T = int(input())
for _ in range(T):
    n = int(input())
    warriors = []
    for __ in range(n):
        warriors.insert(0, input())
    prev = '0000000000'
    for warrior in warriors:
        result = ''
        for index in range(len(prev)):
            if prev[index] == warrior[index]:
                result+='0'
            else:
                result+='1'
        prev = result
    count = 0
    for x in prev:
        if x == '1':
            count+=1
    print(count)