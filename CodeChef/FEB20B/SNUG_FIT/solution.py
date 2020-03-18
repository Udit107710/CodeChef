from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))
    a.sort()
    b.sort()
    s = 0
    for i in range(n):
        s+=min([a[i],b[i]])
    print(s)