from sys import stdin

t = int(stdin.readline())

for _ in range(t):
    a, b = map(int, stdin.readline().split())
    a-=1
    b-=1
    count = 1
    for i in range(2, a+b+1):
        if a%i == b%i:
            count+=1
    print(count)