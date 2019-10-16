N, D = map(int, input().split())
chopsticks = []
for _ in range(N):
    chopsticks.append(int(input()))
chopsticks.sort()
ans = 0
i=0
while(i<N-1):
        if (chopsticks[i+1] - chopsticks[i]) <= D:
            i+=1
            ans+=1
        i+=1

print(ans)