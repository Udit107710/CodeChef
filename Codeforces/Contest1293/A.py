from sys import stdin, stdout

t = int(stdin.readline())

for _ in range(t):
    n, s, k = map(int, stdin.readline().split())

    closed = list(map(int, stdin.readline().split()))
    closed = list(map(lambda x: x-1, closed))
        
    s-=1

    for steps in range(n):
        if (s-steps >= 0) and (s-steps) not in closed:
            break
        if  (s+steps < n) and (s+steps) not in closed:
            break
    
    print(steps)
