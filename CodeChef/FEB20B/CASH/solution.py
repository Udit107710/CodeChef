from sys import stdin

for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    coins = list(map(int, stdin.readline().split()))

    s = sum(coins)
    print(s%k)