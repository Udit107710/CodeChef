from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    score = list(map(int,list(stdin.readline()[0:-1])))
    a = 0
    b = 0
    t = 0
    chanceA = n
    chanceB = n
    flag = False
    val = -1
    for i in range(2*n):
        if i%2 == 0:
            chanceA-=1
            if score[i] == 1:
                a+=1
        else :
            chanceB-=1
            if score[i] == 1:
                b+=1
        
        if (b > a and chanceA < b-a) or (a > b and chanceB < a-b):
            flag = True
            val = i+1
            break
    
    if flag:
        print(val)
    else:
        print(2*n)
