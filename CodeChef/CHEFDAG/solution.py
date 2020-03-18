from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    graph = {}
    for i in range(n):
        graph[i+1] = set(range(1, n+1))
    
    for __ in range(k):
        order = list(map(int, stdin.readline().split()))
        for i in range(n):
            graph[order[i]] = set(order[0:i]) & graph[order[i]]
    for i in range(n):
        for j in range(i+1, n):
            if graph[i+1]:
                graph[i+1] = graph[i+1].discard(graph[j+1])
    empty = 0
    nodes = [0]*n
    for key, value in graph.items():
        if value:
            for v in value:
                nodes[v-1] = key
        else:
            empty+=1
    print(empty)
    print(*nodes)