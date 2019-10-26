T = int(input())

for _ in range(T):
    n, k = map(int, input().split())
    seq = list(map(int, input().split()))
    length = len(seq)
    found = 0
    found_again = 0
    for i in range(0, length):
        for j in range(0, length):
            if seq[i] > seq[j] and i < j:
                found+=1
            elif seq[i] > seq[j]:
                found_again +=1
    
    answer = int(found * ((k*(k+1))/2))
    answer += int((found_again) * ((k*(k+1)/2) - k))
    print(answer)