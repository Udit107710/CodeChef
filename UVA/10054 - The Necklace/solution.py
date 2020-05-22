
def find_euler(euler, start, edges):
    for e in edges[start]:
        if e[1]:
            v = e[0]
            e[1] = False
            for e2 in edges[v]:
                if e2[0] == start and e2[1]:
                    e2[1] = False
                    break
            euler.append([start, v])
            find_euler(euler, v, edges)

t = int(input())
for _ in range(t):
    n = int(input())
    edges = [[]*50 for _ in range(50)]
    degree = [0]*n
    for __ in range(n):
        e = list(map(int, input().split()))
        edges[e[0]-1].append([e[1]-1, True])
        edges[e[1]-1].append([e[0]-1, True])
        degree[e[0]-1]+=1
        degree[e[1]-1]+=1
    
    good = True
    start = -1
    print(degree)
    for deg in range(len(degree)):
        if degree[deg] % 2:
            good = False
            break
        elif degree[deg] > 0 and start == -1:
            start = deg
    print("Case #"+str(t))
    if not good:
        print("some beads may be lost")
    
    euler = []
    find_euler(euler, start, edges)
    print(edges)
    print(euler)