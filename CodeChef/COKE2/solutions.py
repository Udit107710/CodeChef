T = int(input())
for _ in range(T):
    N, Q, K, L, R = map(int, input().split())
    temp_price = []
    for __ in  range(N):
        temp_price.append(list(map(int, input().split())))
    solutions = []
    for i in range(1, Q+1):
        min_temp = 10000
        min_price = 10000
        for temperature, price in temp_price:
            M = i
            while( M >  0):
                if temperature > K+1:
                    temperature-=1
                elif temperature < K-1:
                    temperature+=1
                elif temperature <= K+1 and K-1 <= temperature:
                    temperature = K
                M-=1
            if temperature >= L and temperature <= R and price < min_price:
                min_price = price
        if min_price < 10000:
            solutions.append(min_price)
        else:
            solutions.append(-1)
    print(' '.join(map(str,solutions)))