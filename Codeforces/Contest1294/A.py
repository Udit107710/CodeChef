from sys import stdin
t = int(stdin.readline())

for _ in range(t):
    coins = list(map(int, stdin.readline().split()))
    n = coins.pop(-1)
    p = max(coins)
    arr = [p-c for c in coins]
    r = sum(arr)
    if n-r < 0:
        print("NO")
    elif (n-r)%3 == 0:
        print("Yes")
    else:
        print("No")