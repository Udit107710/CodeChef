from sys import stdin, stdout

t = int(stdin.readline())

for _ in range(t):
    a, m = map(int, stdin.readline().split())

    x = int(m/a)
    answers = []
    length = 0
    for n in range(x, 0, -1):
        t = m - a*n
        if t > n:
            break
        if t <= 0:
            continue
        if (n%t == 0):
            length +=1
            answers.insert(0, n)
        
    stdout.write(str(length) +'\n')
    print(*answers)