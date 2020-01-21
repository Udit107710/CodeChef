from sys import stdin

def cal(p, arr):
    if p == 1:
        return float(1)
    elif arr[p]:
        return arr[p]
    else:
        arr[p] = 1/p + cal(p-1, arr)
        return arr[p]

n = int(stdin.readline())
arr = [False] * (n+1)
arr[0] = 0
for index in range(1,n+1):
    arr[index] = arr[index-1] + 1/index
print(arr[-1])