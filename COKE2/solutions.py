T = int(input())
for _ in range(T):
    N,Q,K,L,R = map(int, input().split())
    temp_cost_list = []

    for __ in range(N):
        temp, cost = map(int, input().split())
        temp_cost_list.append((temp, cost))
    if Q > N:
        for __ in range(N):
            M = __
            temp, cost = temp_cost_list[M]
            for _ in range(M+1):
                if temp > K + 1:
                    temp -= 1
                elif temp < K - 1:
                    temp += 1
                else:
                    temp = K        
            if temp <= R and temp >= L:
                print(cost, end=' ')
            else:
                print(-1)
        for __ in range(Q-N):
            print(-1, end=' ')
    else:
        for __ in range(Q):
            M = __
            temp, cost = temp_cost_list[M]
            for _ in range(M+1):
                if temp > K + 1:
                    temp -= 1
                elif temp < K - 1:
                    temp += 1
                else:
                    temp = K
            if temp <= R and temp >= L:
                print(cost, end=' ')
            else:
                print(-1, end=' ')

    print('')