from sys import stdin, stdout

num_to_bits =[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]
def countSetBitsRec(num): 
    n = 0; 
    if(0 == num): 
        return num_to_bits[0]; 
      
    n = num & 0xf; 

    return num_to_bits[n] + countSetBitsRec(num >> 4)

for _ in range(int(stdin.readline())):
    n, q = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    for __ in range(q):
        query = int(stdin.readline())
        even = 0
        odd = 0
        for i in a:
            if countSetBitsRec(query^i)%2 == 0:
                even+=1
            else:
                odd+=1
        stdout.write(str(even) + ' ' + str(odd) + '\n')