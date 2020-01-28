from sys import stdin

def move(parent, current, k, floors, jumps, n, visited):
    try:
        if floors[parent][current]  and not visited[current]:
            visited[current] = True
            if current == n:
                visited = [False]*(n+1)
                return jumps
            x = 1000000000
            for t in k:
                val = move(current, current + t, k, floors, jumps+1, n, visited)
                print(current, current+t, val)
                if val is not -1:
                    if val < x:
                        x = val
                
            if x == 1000000000:
                return -1
            else:
                return x
        return -1
    except:
        return -1


for _ in range(int(stdin.readline())):
    n, k = map(int, stdin.readline().split())
    floors = []
    for __ in range(n):
        a = list(stdin.readline())
        t = [True if i == '1' else False for i in a[0:-1]]
        floors.append(t)
        print(floors)
    p = list(range(k, -k, -1))
    p.remove(0)
    visited = [False]*n
    print(move(0, 0, p, floors, 0, n-1, visited))