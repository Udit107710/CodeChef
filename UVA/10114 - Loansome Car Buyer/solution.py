from sys import stdin, stdout
while(True):
    try:
        duration, down_payment, loan, records = map(float, stdin.readline().split())
    except:
        break
    if duration < 0:
        break
    duration = int(duration)
    records = int(records)
    dep_percent = [None] * (duration+1)
    for _ in range(records):
        index, percent = map(float, stdin.readline().split())
        index = int(index)
        dep_percent[index] = percent
    prev_dep = dep_percent[0]
    for x in range(0, duration+1):
        if dep_percent[x] is None:
            dep_percent[x] = prev_dep
        else:
            prev_dep = dep_percent[x]
    
    value = down_payment + loan
    month = 0
    value = value - (dep_percent[month] * value)
    owes = loan
    print(dep_percent)
    print(value, owes)
    while(value < owes):
        month+=1
        value = value - (dep_percent[month] * value)
        owes = owes - down_payment
        print(value, owes)
    if month == 1:
        print("1 month")
    else:
        print(str(month)+ " months")