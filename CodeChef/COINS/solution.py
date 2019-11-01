from math import floor
from sys import stdin
dp = {}
for x in range(0,12):
    dp[x] = x
def exchange(coins):
    if coins in dp.keys():
        return dp[coins]
    else:
        ans = max(coins, exchange(floor(coins/2)) + exchange(floor(coins/3)) + exchange(floor(coins/4)))
        dp[coins] = ans
        return ans

for x in stdin:
    x = int(x)
    print(exchange(x))