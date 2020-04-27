from collections import defaultdict

def get_schedule(start, current, time, edges, end):
    if current == end:
        return time, time
    min_time = float("inf")
    start_time = float("inf")
    for e in edges[current]:
        if int(e[0]) >= time:
            t, t1 = get_schedule(start, e[2], int(e[1]), edges, end)
            if t < min_time:
                min_time = t
                start_time = int(e[0])
            if t == min_time and int(e[0]) > start_time:
                start_time = int(e[0])
    
    return min_time, start_time 
 
for _ in range(int(input())):
    c = int(input())
    cities = []
    for __ in range(c):
        cities.append(input())
    
    t = int(input())
    trains = defaultdict(list)

    for __ in range(t):
        train = []
        for ___ in range(int(input())):
            train.append(input().split())
        for q in range(len(train)-1):
            trains[train[q][1]].append([train[q][0], *train[q+1]])

    start_time = input()
    start_place = input()
    end = input()
    t1, t2 = get_schedule(start_place, start_place, int(start_time), trains, end)
    print("Scenario "+str(_+1))
    if t1 == float("inf"):
        print("No connection")
    else:
        print("Departure " + str(t2).zfill(4) + " " + start_place)
        print("Arrival " + str(t1).zfill(4) + " " + end)
    print("")