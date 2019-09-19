T = int(input())
answers = []
for _ in range(T):
    N, M, K, L, R = map(int, input().split())
    temp_cost_list = []
    cost_answer = 10e12
    changed = 0

    for _ in range(N):
        temp, cost = map(int, input().split())
        temp_cost_list.append((temp, cost))

    for temp, cost in temp_cost_list:
        for _ in range(M):
            if temp > K + 1:
                temp -= 1
            elif temp < K - 1:
                temp += 1
            else:
                temp = K
        if temp <= R and temp >= L and cost < cost_answer:
            changed = 1
            cost_answer = cost
    
    if changed:
        answers.append(cost_answer)
    else:
        answers.append(-1)

print('\n'.join(map(str,answers)))
