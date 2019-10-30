T = int(input())
for _ in range(T):
    N_and_speed = list(map(int, input().split()))
    del N_and_speed[0]
    print("Case "+str(_+1)+": "+str(max(N_and_speed)))