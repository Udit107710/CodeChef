from sys import stdin
import numpy as np
n, q = map(int, stdin.readline().split())
coins = []
coins = np.zeros(n, dtype=bool)
for _ in range(q):
    digit, a, b = map(int, stdin.readline().split())
    if digit == 0: 
        coins[a:b+1] = ~coins[a:b+1]  
    else:
        print(coins[a:b+1].sum())