from collections import Counter

T = int(input())
for _ in range(T):
    no = int(input())
    carry = 0
    while(no > 2048):
        no-= 2048
        carry+=1
    binary = bin(no)    
    count = Counter(binary)
    print(int(count["1"])+carry)