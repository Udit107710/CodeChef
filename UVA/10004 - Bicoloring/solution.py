from sys import stdin, stdout

while True:
    v = int(stdin.readline())
    if v > 0:
        e = int(stdin.readline())
        adj_list = [[] * v for _ in range(v)]
        for _ in range(e):
            e1, e2 = map(int, stdin.readline().split())
            adj_list[e1].append(e2)
        
        colored = [None] * v
        queue = [0]
        colored[0] = 0
        clear = True
        reached = [False] * v

        while queue:
            node = queue.pop(0)
            for vertex in adj_list[node]:
                if colored[node] == 0 and (colored[vertex] == None or colored[vertex] == 1):
                    colored[vertex] = 1
                    queue.append(vertex)
                elif colored[node] == 1 and (colored[vertex] == 0 or colored[vertex] == None):
                    colored[vertex] = 0
                    queue.append(vertex)
                else:
                    clear = False
                    queue.clear()
                    break
                
            if not reached[node]:
                reached[node] = True
            else:
                break
        if clear:
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")
    else:
        break