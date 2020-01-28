from sys import stdin

t, x = map(int, stdin.readline())
arr = []
for _ in range(t):
    arr.append(int(stdin.readline()))
    new_arr = sorted(arr)
        