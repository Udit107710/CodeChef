from sys import stdin 
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())

    profit = -1
    for __ in range(n):
        food = list(map(int, stdin.readline().split()))

        p = (food[1]//(food[0]+1)) * food[2]
        if p > profit:
            profit = p
    print(profit)