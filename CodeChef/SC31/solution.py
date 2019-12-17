from sys import stdin, stdout
T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    warriors = []
    prev = '0000000000'
    
    for __ in range(n):
        result = ''
        warrior = stdin.readline()
        for index in range(10):
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