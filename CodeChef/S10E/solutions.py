T = int(input())
for _ in range(T):
    ans = 1
    size_ = int(input())
    prices = list(map(int, input().split()))

    for __ in range(0, 6):
        prices.insert(0, 800)
    
    x = -1
    list_of_tuples = []
    for price in prices:
        list_of_tuples.append((price, x+1))
        x+=1

    ans = 1
    
    for i in range(7, len(prices)):
        if sorted(list_of_tuples[i-5:i+1], key=lambda x: x[0])[0][1] == i:
            ans += 1
    
    print(ans)