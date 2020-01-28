from sys import stdin
for _ in range(int(stdin.readline())):
    n, m, w, h = map(int, stdin.readline().split())
    operation = list(stdin.readline())
    distance = 10000000000
    coords = []
    for __ in range(m):
        x, y = map(int, stdin.readline().split())
        if 'R' in operation:
            d1 = 2 * abs(w - x)
            if distance > d1:
                distance = d1
        if 'U' in operation:
            d2 = 2 * abs(h - y)
            if distance > d2:
                distance = d2
        if 'L' in operation:
            d3 = 2 * x
            if distance > d3:
                distance = d3
        if 'D' in operation:
            d4 = 2 * y
            if distance > d4:
                distance = d4        
        coords.append([x,y])
    c = sorted(coords, key=lambda x: x[0])
    for index in range(1, m):
        d = ((c[index][0] - c[index-1][0])**2 + (c[index][1] - c[index-1][1])**2)**0.5
        if d < distance:
            distance = d
    print(distance)