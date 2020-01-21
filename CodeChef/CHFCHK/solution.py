from sys import stdin
t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    fav = list(map(int, stdin.readline().split()))
    print(min(fav))