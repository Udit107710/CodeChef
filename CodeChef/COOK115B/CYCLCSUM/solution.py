from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    arr = list(map(int, list(stdin.readline().split())))
    m = -1000000000
    s = [0]*n
    s[0] = arr[0]
    for i in range(1, n):
        if s[i-1]+arr[i] > arr[i]:
            s[i] = s[i-1]+arr[i]
        else:
            s[i] = arr[i]
        if s[i] > m:
            m = s[i]
    print(m, end= ' ')
    for i in range(1, n):
        if arr[i] == s[1]:
            t = s.pop(0)
            s.append(s[-1]+t)
            print(m, end=' ')
        else:
            p = -1
            for k in range(1, n):
                if k - i < 0:
                    k = k - i + n
                if s[k] - s[k-1] == arr[k]:
                    continue
                else:
                    p = k
                    break
            t = s.pop(0)
            a = lambda x : x - t
            if p == -1:
                s = list(map(a, s))
            else:
                s[0:p] = list(map(a,s[0:p]))
            if s[-1]+t > t:
                s.append(s[-1]+t)
            else:
                s.append(t)

            m = max(s)
            print(m, end=' ')
    print('')
