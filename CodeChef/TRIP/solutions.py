T = int(input())

for _ in range(T):
    N, K =  map(int, input().split())
    array = list(map(int, input().split()))
    places = range(1,K+1)
    for index in range(len(array)):
        if array[index] < 0:
            not_allowed = []
            try:
                if array[index-1]:
                    not_allowed.append(array[index-1])
            except:
                pass
            try:
                if array[index+1]:
                    not_allowed.append(array[index+1])
            except:
                pass
            allowed = [x if x not in not_allowed else None for x in places]
            for element in allowed:
                if element:
                    array[index] = element
                    break
    if -1 in array:
        print('NO')
    else:
        print('YES')
        print(*array)