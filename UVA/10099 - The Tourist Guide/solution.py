from sys import stdin, stdout
from math import ceil
no = 0
while True:
    no += 1
    n, r = map(int, stdin.readline().split())
    if n == 0 and r == 0:
        break
    adj_matrix = [[-1]*n for _ in range(n)]

    for _ in range(r):
        v1, v2, cost = map(int, stdin.readline().split())
        adj_matrix[v1-1][v2-1] = cost - 1
        adj_matrix[v2-1][v1-1] = cost - 1
    
    start, destination, travellers = map(int, stdin.readline().split())
    start -= 1
    destination -= 1
    
    sum_cost = [-1] * n
    stack = [(float("inf"),start)]
    min_cost = -1
    
    while stack:
        c, node = stack.pop(0)
        if node != destination:
            for vertex in range(n):
                path = adj_matrix[node][vertex]
                if vertex == start:
                    continue
                if path > -1:
                    prev = sum_cost[vertex]
                    new = min([path, c])
                    sum_cost[vertex] = max([prev, new])
                    if prev < sum_cost[vertex]:
                        stack.append((sum_cost[vertex], vertex))
        else:
            if min_cost < c:
                min_cost = c
    
    stdout.write("Scenario #"+str(no) + "\n")
    stdout.write("Minimum Number of Trips = " + str(ceil(travellers/min_cost)) + "\n\n")