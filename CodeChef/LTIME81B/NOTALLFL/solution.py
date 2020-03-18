for _ in range(int(input())):
    n,k = map(int, input().split())
    seq = list(map(int, input().split()))
    flag = False
    occ = {}
    val = -1
    for t in range(k):
        occ[t+1] = [-1]
    for i in range(n):
        occ[seq[i]].append(i)
    for t in range(k):
        occ[t+1].append(n)
    for key, value in occ.items():
        length = len(value)
        if length == 1:
            val = n
            break
        for j in range(length-1):
            if val < value[j+1] - value[j] - 1:
                val = value[j+1] - value[j] - 1
    print(val)