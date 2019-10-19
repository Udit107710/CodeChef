for _ in range(int(input())):
    N = int(input())
    
    inputs = []
    for __ in range(N):
        inputs.append(tuple(input().split()))
    
    ans = {}
    x = 0
    for key, value in inputs:
        if key in ans.keys():
            if value == '0':
                ans[key][1]+=1
            else:
                ans[key][2]+=1
        else:
            
            if value == '0':
                ans[key] = [value, 1, 0]
            else:
                ans[key] = [value, 0, 1]
        
    for value in ans.values():
        x+=max(value[1:])

    
    print(x)