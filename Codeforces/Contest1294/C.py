from sys import stdin
t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    if n < 24:
        print("NO")
        continue
    a = []
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            n//=i
            a.append(i)
            break
    if len(a) == 1:
        for i in range(a[0]+1, int(n**0.5)+1):
            if n%i == 0:
                n//=i
                a.append(i)
                break
    a.append(n)
    if len(a) == 3 and a[1] < a[2]:
        print("YES")
        print(*a)
    else:
        print("NO")