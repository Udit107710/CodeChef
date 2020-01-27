from sys import stdin 
from collections import defaultdict
f = open("sol.txt", "a+")

while True:
    v = int(stdin.readline())
    if v > 0:
        e = int(stdin.readline())
        adj_list = [[] * v for _ in range(v)]
        for _ in range(e):
            e1, e2 = map(int, stdin.readline().split())
            adj_list[e1].append(e2)
            adj_list[e2].append(e1)
        
        queue = [[0,0]]
        clear = True
        reached = [False] * v
        heights = defaultdict(int)
        heights[0] = 0

        while queue:
            node, height = queue.pop(0)
            for n in adj_list[node]:
                if not reached[n]:
                    queue.append([n,height+1])
                    heights[n] = height+1
                    reached[n] = True
        
        clear = True
        for n in range(v):
            for p in adj_list[n]:
                if heights[p] == heights[n]:
                    clear = False
                    break
        if clear:
            f.writelines("BICOLORABLE.\n")
            print("BICOLORABLE.")
        else:
            f.writelines("NOT BICOLORABLE.\n")
            print("NOT BICOLORABLE.")
    else:
        break