from sys import stdin
t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    arr = []
    for __ in range(n):
        arr.append(list(map(int, stdin.readline().split())))
    arr_sorted = sorted(arr)
    flag = False
    order = ''
    order += 'R'*arr_sorted[0][0]
    order += 'U'*arr_sorted[0][1]
    for index in range(1, n):
        if arr_sorted[index][1] < arr_sorted[index-1][1]:
            flag = True
            break         
        order += 'R'*(arr_sorted[index][0] - arr_sorted[index-1][0])
        order += 'U'*(arr_sorted[index][1] - arr_sorted[index-1][1])
    
    if flag:
        print("NO")
    else:
        print("YES")
        print(order)
        
        