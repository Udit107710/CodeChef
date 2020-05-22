for _ in range(int(input())):
    n = int(input())
    people = list(map(int, input().split()))
    last = -6
    found = False
    for index in range(n):
        if people[index] == 1:
            if index-last < 6:
                found = True
                break
            last = index
    if found:
        print("NO")
    else:
        print("YES")