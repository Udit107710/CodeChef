from collections import defaultdict

for _ in range(int(input())):
    n, m = map(int, input().split())
    fruits = list(map(int, input().split()))
    cost = list(map(int, input().split()))
    c = defaultdict(int)

    for i in range(n):
        c[fruits[i]]+=cost[i]

    print(min(c.values()))