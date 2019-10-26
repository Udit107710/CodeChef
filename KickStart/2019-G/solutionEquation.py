T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    sum_ = 0
    for x in numbers:
        sum_ += (x | 0)
    if sum_ <= N:
        print(-1)
        