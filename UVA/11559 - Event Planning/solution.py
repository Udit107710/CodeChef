from sys import stdin, stdout
while(True):
    try:
        N, budget, hotels, weeks = map(int, stdin.readline().split())
    except:
        break
    cost = []
    for _ in range(hotels):
        rate = int(stdin.readline())
        availabiltiy = list(map(int, stdin.readline().split()))
        if any([True if x >= N else False for x in availabiltiy]):
            if rate*N <= budget:
                cost.insert(0, rate*N)
    if len(cost) > 0:
        print(min(cost))
    else:
        print("stay home")