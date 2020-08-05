"""
This file is responsible to decide which config will be crawled.
A config that crawls more tenders will be scheduled more often.
"""

import os
import logging
from datetime import datetime
from time import sleep
from math import log, ceil

from django.utils import timezone
from pg_python import pg_python
from db_configuration import postgres, constants

"""
table has columns: slot_id, config_id, is_picked, time_picked, last_reset, picked_by
"""

on_conflict_query = ' on conflict(slot_id) do update set slot_id=excluded.slot_id, config_id=excluded.config_id'
table_columns = ('slot_id', 'config_id')
cron_scheduler_query = """update cron_scheduler set last_crawled=now() where id in (SELECT id from cron_scheduler where
 (now()::date >= last_crawled::date + days or last_crawled is null) and is_active=true and is_exclude_scheduling =false) 
 returning config_id"""
sub_query_format = """(select config_id, count(*) from %s where config_id in (%s) and retrieved_on >= now() - interval '
%s days' group by config_id)"""


def process_scheduling():
    logging.info('processing schedule')
    active_configs_set, schema_list = _get_active_configs_db()
    config_frequencies = _get_config_frequencies_db(active_configs_set, schema_list)

    if active_configs_set in constants.none_list:
        logging.error("Couldn't retrieve active configs")

    if config_frequencies in constants.none_list:
        logging.error("Couldn't retrieve tender data")

    freq_dict = _create_config_frequency_dict(config_frequencies, active_configs_set)
    slots = _create_schedule(freq_dict)

    if slots in constants.none_list:
        logging.error("failed to create slots")
        return

    ret_val = _update_schedule_db(slots)
    if ret_val in constants.none_list:
        logging.error("failed to write slots to database")
        return

    ret_val = _reset_ids()
    if ret_val in constants.none_list:
        logging.error("failed to reset is_picked")
        return

    logging.info("successfully reset schedule")
    return True


def _find_ids():
    """
    Find the slot_id & config_id for first slot that has not been run
    :return: slot_id, config_id
    """
    r = pg_python.read(constants.schedule_table, ["slot_id", "config_id"],
                       {"is_picked": False}, limit=1, order_by="slot_id", order_type="asc",
                       server=postgres.DASHBOARD_DB)
    if r in constants.none_list:
        return None, None

    slot_id = int(r[0]['slot_id'])
    config_id = int(r[0]["config_id"])

    return slot_id, config_id


def _reset_ids():
    # Set is_picked to False for all slots.
    reset_query = "UPDATE " + constants.schedule_table + " SET is_picked = false,last_reset = %s "
    ret_val = pg_python.write_raw(reset_query, [timezone.now()], server=postgres.DASHBOARD_DB)
    if not ret_val:
        logging.debug("Config Update failed!")
    return ret_val


def _reserve_config(slot_id):
    ret_val = pg_python.update(constants.schedule_table, {"is_picked": True}, {"slot_id": slot_id},
                               server=postgres.DASHBOARD_DB)
    if not ret_val:
        logging.debug("Config Reservation failed!")
    return ret_val


def _get_scheduling_frequency(tender_count, log_base=2):
    # how many slots will a config get based on how many tenders it could retrieve
    return max(1, int(ceil(log(tender_count + 0.01, log_base))))


def _get_active_configs_db():
    keys = [constants.COL_CONFIG_ID, constants.SCHEMA]
    where_map = dict()
    where_map[constants.COL_IS_ACTIVE] = True
    where_map[constants.COL_IS_EXCLUDE_SCHEDULING] = False
    rows = pg_python.read(constants.crawler_configs, keys, where_map, server=postgres.DASHBOARD_DB)
    if rows in constants.none_list:
        logging.error("Couldn't find any active configs")
        return
    active_configs_set = set()
    schema_list = set()
    for row in rows:
        active_configs_set.add(row[constants.COL_CONFIG_ID])
        schema_list.add(row[constants.SCHEMA])
    return active_configs_set, schema_list


def get_cron_configs():
    cron_configs = set()
    db = pg_python.get_db(postgres.DASHBOARD_DB)
    cur = db.get_cursor()
    cur.execute(cron_scheduler_query)
    result = cur.fetchall()
    db.connection.commit()
    if result:
        for val in result:
            cron_configs.add(str(val[0]))
    return cron_configs


def _get_config_frequencies_db(active_configs, schema_list, days=30):
    # Gives all configs and how many tenders each of them retrieved
    active_configs_string = ','.join(active_configs)
    frequency_query = " UNION ".join(
        [sub_query_format % (schema, active_configs_string, days) for schema in schema_list])
    rows = pg_python.read_raw(frequency_query, None, server=postgres.SERVER_WRITE)
    if rows in constants.none_list:
        logging.error("Couldn't get any configs")
        return
    count_dict = dict()
    for row in rows:
        config_id = str(row[0])
        count = int(row[1])
        count_dict[config_id] = count_dict[config_id] + count if count_dict.get(config_id, None) else count
    return count_dict


def _create_config_frequency_dict(config_frequencies, active_configs_set):
    """
    :param config_frequencies: List of tuples. Configs with how many tenders it retrieved.
    :param active_configs_set: Set of all active configs
    :return: dictionary => keys: configs, values: how many slots that config will get
    """

    freq_dict = {}
    for config_id, tender_freq in config_frequencies.items():
        no_of_slots = _get_scheduling_frequency(tender_freq)
        freq_dict[config_id] = no_of_slots
    cron_configs = get_cron_configs()
    picked_configs = set(config_frequencies.keys())
    unpicked_configs = active_configs_set - picked_configs
    unpicked_configs = unpicked_configs.union(cron_configs)
    # ensure each config is scheduled at least once
    for config_id in unpicked_configs:
        freq_dict[config_id] = 1
    return freq_dict


def _get_step(total_slots, freq):
    # After how many configs should this config be scheduled
    return int(round(float(total_slots) / float(freq)))


def _create_schedule(freq_dict):
    logging.info("Creating schedule")
    total_slots = sum(freq_dict.values())
    slots = [False] * total_slots  # create empty slots

    config_list = sorted(freq_dict.keys(),
                         key=lambda config_id: freq_dict[config_id],
                         reverse=False)

    for config_id in config_list:
        freq = freq_dict[config_id]
        step = _get_step(total_slots, freq)

        for i in range(0, total_slots, step):
            while i < total_slots:
                if not slots[i]:
                    slots[i] = config_id
                    break
                i += 1  # Look for an empty slot

    # Some configs may have not been scheduled
    scheduled_configs = set(slots)
    unscheduled_configs = set(config_list) - scheduled_configs
    for config_id in unscheduled_configs:
        slots.append(config_id)
    # total number of slots will increase but that is intended. will happen rarely
    return slots


def _update_schedule_db(slots):
    # STEP 1 :  How many slots are currently in the table?

    total_slots_query = """SELECT COUNT(*) from %s""" % constants.schedule_table
    rows = pg_python.read_raw(total_slots_query, None, server=postgres.DASHBOARD_DB)
    if rows in constants.none_list:
        logging.error("Failed to read scheduling table")
        return
    total_slots_db = int(rows[0][0])
    if total_slots_db > len(slots):
        slots = slots + [-1] * (total_slots_db - len(slots))
    slots_dict_list = [dict(zip(table_columns, (slot_id + 1, config_id))) for slot_id, config_id in enumerate(slots)]
    slots_insert_statement, values = pg_python.make_postgres_write_multiple_statement(constants.schedule_table,
                                                                                      table_columns, slots_dict_list)
    slots_insert_statement = slots_insert_statement + on_conflict_query
    ret_val = pg_python.write_raw(slots_insert_statement, values, server=postgres.DASHBOARD_DB)
    if ret_val:
        logging.info(
            "Successfully updated schedule. Total slots changed from %s to %s" % (str(total_slots_db), str(len(slots))))
    return True


def get_url_list(result):
    links = list()
    for res in result:
        links.append(res[0])
    return links


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    postgres.connect_db(server=postgres.DASHBOARD_DB)
    postgres.connect_db(server=postgres.SERVER_WRITE)
    process_scheduling()
