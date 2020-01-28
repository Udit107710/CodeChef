from sys import stdin
for _ in range(int(stdin.readline())):
    n, a, b, c = map(int, stdin.readline().split())
    f = list(map(int, stdin.readline().split()))
    index = -1

    if a - b > 0:
        for i in range(n):
            if f[i] <= a and f[i] >= b:
                index = i
                break
    else:
        for i in range(n):
            if f[i] >= a and f[i] <= b:
                index = i
                break
    if index >= 0:
        print(abs(b-a)+c)
    else:
        dist = [abs(x-b) for x in f]
        index = dist.index(min(dist))
        print(abs(f[index]-b)+abs(f[index]-a)+c)
