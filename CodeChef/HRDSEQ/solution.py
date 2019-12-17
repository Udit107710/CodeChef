from sys import stdin
T = int(stdin.readline())
for _ in range(T):
    n = int(stdin.readline())
    sequence = [0]
    occur = {0:[0]}
    for index in range(n-1):
        prev_element = sequence[index]
        if len(occur[prev_element]) > 1:
            new_element = occur[prev_element][-1] - occur[prev_element][-2]
            sequence.append(new_element)
            try:
                occur[new_element].append(index+1)
            except:
                occur[new_element] = [index+1]
        else:
            sequence.append(0)
            occur[0].append(index+1)
    print(len(occur[sequence[-1]]))