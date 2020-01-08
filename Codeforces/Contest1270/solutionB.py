from sys import stdin, stdout
import sys
t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    array = list(map(int, stdin.readline().split()))

    max_ = -1
    min_ = 10000000000

    max_array_1 = [0] * n
    min_array_1 = [0] * n

    for index in range(n):
        max_array_1[index] = max(max_, array[index])
        min_array_1[index] = min(min_, array[index])

        max_ = max_array_1[index]
        min_ = min_array_1[index]
    
    max_ = -1
    min_ = 10000000000
    
    max_array_2 = [0] * n
    min_array_2 = [0] * n

    for index in range(n-1, -1, -1):
        max_array_2[index] = max(max_, array[index])
        min_array_2[index] = min(min_, array[index])

        max_ = max_array_2[index]
        min_ = min_array_2[index]
    
    print(min_array_1, max_array_1)
    print(min_array_2, max_array_2)
