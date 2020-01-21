from sys import stdin

n, q = map(int, stdin.readline().split())

maze = [[True]*n for _ in range(2)]

for _ in range(q):
    i,j = map(int, stdin.readline().split())
    i-=1
    j-=1
    maze[i][j] = not maze[i][j]
    status = True
    if not (maze[1][n-2] or maze[0][n-1]):
        status = False
    if status:
        for p in range(1,n):
            if (maze[0][p] or maze[1][p]) and (maze[1][p-1] or maze[0][p]) and (maze[0][p] or maze[1][p+1]):
                continue
            else:
                status = False
                break
    if status:
        print("Yes")
    else:
        print("No")