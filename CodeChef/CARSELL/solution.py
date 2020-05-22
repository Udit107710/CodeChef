for _ in range(int(input())):
    n = int(input())
    cars = list(map(int, input().split()))
    cars = sorted(cars, reverse=True)
    c = [0 if cars[i]-i  < 0 else cars[i]-i for i in range(n)]
    print(sum(c)%(10**9+7))