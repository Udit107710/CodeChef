from sys import stdin

for _ in range(int(stdin.readline())):
    n, p = map(int, stdin.readline().split())
    coins = list(map(int, list(stdin.readline().split())))
    count = [0]*n
    # for i in range(n):
    #     if p%coins[i] == 0:
    #         count[i] = 0
    #     else:
    #         if p > 0:
    #             count[i] = (int(p/coins[i]) + 1)
    #             p-=(count[i]*coins[i])
    #         else:
    #             break
    j = 0
    for i in range(n):
        while p > 0:
            pass
            


    if sum(count) > 0 and p < 0:
        print("YES", *count)
    else:
        print("NO")