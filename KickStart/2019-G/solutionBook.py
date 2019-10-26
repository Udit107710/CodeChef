import numpy as np

T = int(input())
for _ in range(T):
    N, M, Q = map(int, input().split())
    removed = list(map(int, input().split()))
    readers = list(map(int, input().split()))
    
    pages = np.arange(start=1, stop=N+1, step=1)
    read = []
    for reader in readers:
        for i in pages:
            if i%reader == 0:
                read.insert(0, i)

    ans = []
    for x in read:
        if x not in removed:
            ans.append(x)


    print("Case #"+ str(_+1)+': '+str(len(ans)))