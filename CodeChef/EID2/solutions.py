import operator

T = int(input())
answers = []
for _ in range(T):
    a1, a2, a3, c1, c2, c3 = map(int, input().split())
    initial_1 = [a1, a2, a3]
    initial_2 = [c1, c2, c3]
    if len(set(initial_1)) == len(set(initial_2)):
        initial_1 = [(a1, c1), (a2, c2), (a3, c3)]
        initial_2 = initial_1.copy()
        initial_1.sort(key = operator.itemgetter(0))
        initial_2.sort(key = operator.itemgetter(1))
        if initial_2 == initial_1:
            answers.append('FAIR')
        else:
            answers.append('NOT FAIR')
    else:
        answers.append('NOT FAIR')

print('\n'.join(answers))
