import numpy as np

for _ in range(int(input())):
    n = int(input())
    array = np.arange(n+1)
    array = np.delete(array, 0, axis=None)
    days = 0
    if n < 4:
        print(1)
        print(n, *array)
    else:
        ans = []
        start = 0
        end = 3
        days = n // 2
        print(days)
        print(3, 1, 2, 3)
        if n % 2 == 0:
            for i in range(1, days-1):
                print(2, (i+1)*2, (i+1)*2+1)
            print(1, (i+2)*2)
        else:
            for i in range(1, days):
                print(2, (i+1)*2, (i+1)*2+1)