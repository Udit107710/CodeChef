from collections import Counter

for _ in range(int(input())):
    N = int(input())

    inputs = list(map(int, input().split()))

    squares = [2**i for i in range(1,100)]
    answer = 0
    sum__ =  1
    ans = []
    for i in range(len(inputs)):
        sum__ = sum__ | inputs[i]
        obj = Counter(bin(inputs[i])[2:])


        if '0' not in obj.keys():
            obj[0] = 0
        if '1' not in obj.keys():
            obj[1] = 0
        
        if (inputs[i] + 1) in squares:
            ans.append((i,obj['0']+1, obj['1'], inputs[i]))
        else:
            ans.append((i,obj['0'], obj['1'], inputs[i]))

    ans = sorted(ans,key= lambda z : z[1], reverse=True)
    answer += sum__
    for i in range(len(ans)-1):
        if ans[i][1] == ans[i+1][1] and ans[i+1][2] < ans[i][2]:
            temp = ans[i]
            ans[i] = ans[i+1]
            ans[i+1] = temp

    ans.append((0,0,0))
    print(ans)

    for __ in range(N):
        sum__ = 0
        if ans[0][1] == ans[1][1]:
            if ans[0][2] <= ans[1][2]:
                del ans[0]
            else:
                del ans[1]
        else:
            del ans[0]
        
        for i in range(len(ans)):
            sum__ = sum__ | inputs[ans[i][0]]
        answer+= sum__
    
    print(answer)