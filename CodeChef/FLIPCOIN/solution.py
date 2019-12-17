from sys import stdin
n, q = map(int, stdin.readline().split())
coins = [0] * n
while q >0:
    digit, a, b = map(int, stdin.readline().split())
    if digit == 1:  
        print(sum(coins[a:b+1]))
    else:
        for index in range(a, b+1):
            coins[index] = not coins[index]
    q-=1