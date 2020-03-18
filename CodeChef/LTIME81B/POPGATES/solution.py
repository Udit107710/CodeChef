for _ in range(int(input())):
    n, k = map(int, input().split())
    sequence = input().split()
    count = 0
    last = n-1
    for i in range(k):
        if sequence[last] == 'H':
            sequence = ["H" if word == 'T' else 'T' for word in sequence[0:last]]
        last-=1
    h = 0
    for c in sequence[0:n-k]:
        if c == 'H':
            h+=1
    print(h)