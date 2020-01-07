from sys import stdin, stdout

t = int(stdin.readline())

for _ in range(t):
    s, w1, w2, w3 = map(int, stdin.readline().split())
    
    stack = [w1, w2,w3]
    s_temp = s
    times = 1
    while stack:
        print(stack, times, s_temp)
        if stack[0] <= s_temp:
            s_temp -= stack.pop(0)
        else:
            times += 1
            s_temp = s
    
    print(times)