t=int(input())
for _ in range(t):
    n,q=map(int,input().split())
    s=input()
    dp=[0]*(n+1)
    for i in range(n-2):
        p=s[i:i+3]
        if p.count(p[0])>=2 or p.count(p[1])>=2:
            dp[i+1]=dp[i]+1
        else:
            dp[i+1]=dp[i]
    for _ in range(q):
        l,r=map(int,input().split())
        if n<3 or (r-l)<2:
            print("NO")
            continue
        if dp[r-2]-dp[l-1]>0:
            print("YES")
        else:
            print("NO")