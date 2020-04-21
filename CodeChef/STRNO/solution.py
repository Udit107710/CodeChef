from collections import defaultdict
import math

def primeFactors(n, k):
    factors = defaultdict(int)
    while n % 2 == 0: 
        factors[2] += 1
        n = n // 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0: 
            factors[i] +=1 
            n = n / i 
    if n > 2: 
        factors[n] = 1
    
    primes = 0
    for val in factors.values():
        primes += val

    if primes < k:
        return False
    else:
        return True

    
for _ in range(int(input())):
    x, k = map(int, input().split())
    if primeFactors(x,k):
        print(1)
    else:
        print(0)