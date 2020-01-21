from sys import stdin, stdout
from collections import defaultdict

n, q, k = map(int, stdin.readline().split())
shops = defaultdict(list)

for _ in range(n):
    line = stdin.readline().split()
    p = int(line[0])
    l = int(line[2])
    r = int(line[3])
    shops[line[1]].insert(0,[p,l,r])

for _ in range(q):
    line = stdin.readline().split()
    x = int(line[0])
    t = int(line[1])
    possible = True
    distance = 0
    for values in shops.values():
        min_distance = 10000000000
        for value in values:
            if t >= value[1] and t <= value[2]:
                dist = abs(value[0]-x)
                if min_distance > dist:
                    min_distance = dist
        if min_distance == 10000000000:
            possible = False
            break
        distance+=min_distance 
    if possible:
        stdout.write(str(distance)+'\n')
    else:
        stdout.write('-1\n')