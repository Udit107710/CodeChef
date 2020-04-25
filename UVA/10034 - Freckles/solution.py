def distance(a, b):
    r = ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
    return r
t = int(input())
for _ in range(t):
    space = input()
    n = int(input())
    coord = []
    for __ in range(n):
        coord.append(list(map(float, input().split())))
    matrix = [0*n for __ in range(n)]
    for i in range(n):
        dist = []
        for j in range(n):
            if i == j:
                dist.append(float("inf"))
            else:
                dist.append(distance(coord[i], coord[j]))
        matrix[i] = dist
    
    counted = [0]
    dist = 0
    while len(counted) < n:
        min_ = float("inf")
        element = -1
        p = -1
        for i in range(n):
            for j in range(n):
                if matrix[i][j] < min_ and (i in counted and not j in counted):
                    min_ = matrix[i][j]
                    element = j
                    p = i

        counted.append(element)
        dist += min_
        matrix[p][element] = float("inf")
        matrix[element][p] = float("inf")

    if _ == t-1:
        print("{:.2f}".format(dist))
    else:
        print("{:.2f}\n".format(dist))