from sys import stdin
from collections import defaultdict
u = 0

def calculate(arr, p, q, s, c, m):
    if c > 0:
        for i in range(4):
            for j in range(4):
                if (i not in p) and (j not in q):
                    if arr[i][j] == 0:
                        s-=100 
                    else:
                        s+=c*arr[i][j]
                    c-=25
                    q.append(j)
                    p.append(i)
                    ans = calculate(arr, p, q, s, c, m)
                    c+=25
                    if arr[i][j] == 0:
                        s+=100
                    else:
                        s-=c*arr[i][j]
                    if p:
                        p.pop(-1)
                    if q:
                        q.pop(-1)
                    if ans > m:
                        m = ans
        return m
    else:
        return s


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    ticket = [[0]*4 for __ in range(4)]
    # ticket = {"12": [0]*4, "3": [0]*4, "6": [0]*4, "9": [0]*4}
    for __ in range(n):
        c, k = stdin.readline().split()
        if c == "A" and k == "12":
            ticket[0][0]+=1
        elif c == "A" and k == "3":
            ticket[0][1]+=1
        elif c == "A" and k == "6":
            ticket[0][2]+=1
        elif c == "A" and k == "9":
            ticket[0][3]+=1
        elif c == "B" and k == "12":
            ticket[1][0]+=1
        elif c == "B" and k == "3":
            ticket[1][1]+=1
        elif c == "B" and k == "6":
            ticket[1][2]+=1
        elif c == "B" and k == "9":
            ticket[1][3]+=1
        elif c == "C" and k == "12":
            ticket[2][0]+=1
        elif c == "C" and k == "3":
            ticket[2][1]+=1
        elif c == "C" and k == "6":
            ticket[2][2]+=1
        elif c == "C" and k == "9":
            ticket[2][3]+=1
        elif c == "D" and k == "12":
            ticket[3][0]+=1
        elif c == "D" and k == "3":
            ticket[3][1]+=1
        elif c == "D" and k == "6":
            ticket[3][2]+=1
        elif c == "D" and k == "9":
            ticket[3][3]+=1
        
    maxValue = -500
    o = (calculate(ticket, [], [], 0, 100, -500))
    u+=o
    print(o)
print(u)
     