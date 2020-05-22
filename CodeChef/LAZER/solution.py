from sys import stdin, stdout

for _ in range(int(stdin.readline())):
    n, q = map(int, stdin.readline().split())
    points = list(map(int, stdin.readline().split()))

    for __ in range(q):
        x1, x2, y = map(int, stdin.readline().split())
        prev = -1
        count = 0
        for i in range(x1 , x2):
            if (prev == -1 and points[i] >= y and points[i-1] <= y) or (prev == 0 and points[i] >= y):
                count+=1
                prev = 1
            elif (prev == -1 and points[i] <= y and points[i-1] >= y) or (prev == 1 and  points[i] <= y):
                count+=1
                prev = 0
        stdout.writelines(str(count) + "\n")