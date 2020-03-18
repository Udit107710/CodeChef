from sys import stdin
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    tax = 0
    flag = False
    if n > 250000:
        if n <= 500000:
            tax+=(n-250000)*0.05
        else:
            tax+=(250000)*0.05
            if n <= 750000:
                tax+=(n-500000)*0.10
            else:
                tax+=(750000-500000)*0.10
                if n <= 1000000:
                    tax+=(n-750000)*0.15
                else:
                    tax+=(1000000-750000)*0.15
                    if n <= 1250000:
                        tax+=(n-1000000)*0.2
                    else:
                        tax+=(1250000-1000000)*0.2
                        if n <= 1500000:
                            tax+=(n-1250000)*0.25
                        else:
                            tax+=(1500000-1250000)*0.25
                            tax+=(n-1500000)*0.30
    print(int(n-tax))