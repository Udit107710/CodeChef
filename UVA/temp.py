sample = "1 1 0 1 0 1 0 0 0 0 1 1 1 1 1 1 1 1 0 1 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 0 0  1 1 1 1 0 0 1 1 0 1 1 0 0 1 1 1 0 0 1 1 1 1 1 0 0 0 0 0 1 1 1 1 1 1 0 0 0 1 1 0 1 0 1 0 1 0 0 1 0 1 1 0 1 0 1 1 0 1 1 1 0 0 0 0 1 1 1 1 1 0 0 1 0 1 0 1 0 0 1 0 0 1 1 0 1 1 1 1 0 1 0 1 1 1 0 0 0 1 0 0 0 0 0 0 1 0 1 0 1 0 1 0 0 1 1 0 1 0"

array = list(map(int, sample.split()))

n = len(array)

start = 0
end = n-1
while end > start:
    print(array)

    first = array[start]
    last = array[end]

    if first > last:
        array[start] = 0
        array[end] = 1
        start+=1
        end-=1
    elif last > first:
        start+=1
        end-=1
        continue
    elif first == 1:
        end-=1
    else:
        start+=1
print(array)