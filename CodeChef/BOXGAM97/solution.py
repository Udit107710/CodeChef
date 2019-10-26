T = int(input())

for _ in range(T):
    n, k, p = map(int, input().split())
    boxes = list(map(int, input().split()))
    pos = 0
    max_value = 0
    min_value = 10000000000
    min_pos = 0
    max_pos = 0
    length = 0
    for i, val in enumerate(boxes):
        if val < min_value:
            min_value = val
            min_pos = i
        if val > max_value:
            max_value = val
            max_pos = i
        length = i
    length+=1
    if p == 0:
        pos = max_pos
    else:
        pos = min_pos
    k-=1
    while(k>0):
        k-=1
        if p == 0:
            p = 1
            if pos < max_pos:
                pos+=1
            elif pos > max_pos:
                pos-=1
            else:
                if pos-1 >= 0 and pos+1 < length:
                    if boxes[pos-1] < boxes[pos+1]:
                        pos+=1
                    else:
                        pos-=1
                elif pos-1 >= 0:
                    pos-=1
                else:
                    pos+=1
        else:
            p = 0
            if pos < min_pos:
                pos+=1
            elif pos > min_pos:
                pos-=1
            else:
                if pos-1 >= 0 and pos+1 < length:
                    if boxes[pos-1] < boxes[pos+1]:
                        pos-=1
                    else:
                        pos+=1
                elif pos-1 >= 0:
                    pos-=1
                else:
                    pos+=1

    print(boxes[pos])