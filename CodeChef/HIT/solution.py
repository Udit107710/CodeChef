T = int(input())

for _ in range(T):
    n = int(input())
    marks = list(map(int, input().split()))
    length = len(marks)
    marks = sorted(marks)
    parts = int(length/4)
    if marks[parts] == marks[parts-1]:
        print(-1)
        continue
    if marks[2*parts] == marks[2*parts - 1]:
        print(-1)
        continue
    if marks[3*parts] == marks[3*parts - 1]:
        print(-1)
        continue
    print(marks[parts], marks[2*parts], marks[3*parts]) 