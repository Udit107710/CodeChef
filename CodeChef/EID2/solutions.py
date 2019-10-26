T = int(input())
for _ in range(T):
    a1, a2, a3, c1, c2, c3 = map(int, input().split())
    initial_1 = [a1, a2, a3]
    initial_2 = [c1, c2, c3]
    if len(set(initial_1)) == len(set(initial_2)):
        age_money = list(zip(initial_1, initial_2))
        index_1 = sorted(age_money, key=lambda x: x[0])
        index_2 = sorted(age_money, key=lambda x: x[1])
        if index_1 == index_2:
            print('FAIR')
        else:
            print('NOT FAIR')
    else:
        print('NOT FAIR')