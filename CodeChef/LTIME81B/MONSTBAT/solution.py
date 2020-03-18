for _ in range(int(input())):
    n, m = map(int, input().split())
    valueA = list(map(int, input().split()))
    mA = list(input())
    valueB = list(map(int, input().split()))
    mB = list(input())
    defenceA = []
    defenceB = []
    attackA = []
    attackB = []
    A = sum(valueA)
    B = sum(valueB)
    for i in range(n):
        if mA[i] == 'A':
            attackA.append(valueA[i])
        else:
            defenceA.append(valueA[i])
    for i in range(m):
        if mB[i] == 'A':
            attackB.append(valueB[i])
        else:
            defenceB.append(valueB[i])
    defenceB.sort()
    defenceA.sort()
    attackA.sort()
    attackB.sort()
    count = 0
    difference = abs(A-B)
    for i in range(min(n,m)):
        if count%2 == 0:
            if len(defenceB) ==0:
                break
            if len(attackA) == 0:
                break
            val = attackA.pop(0)
            length = len(defenceA)
            for j in range(length):
                if defenceA[j] > val:
                    defenceA.insert(j, val)
                    break
            if len(defenceA) == length:
                defenceA.append(val)
            v = defenceB.pop(-1)
            prev = B
            B-=v
            if A-B < A-prev:
                B = prev
                break
        else:
            if len(defenceA) == 0:
                break
            if len(attackB) == 0:
                break
            val = attackB.pop(0)
            length = len(defenceB)
            for j in range(length):
                if defenceB[j] > val:
                    defenceB.insert(j, val)
                    break
            if len(defenceB) == length:
                defenceB.append(val)
            v = defenceA.pop(-1)
            prev = A
            A-=v
            if B-A < B-prev:
                A = prev
                break
    print(abs(A-B))