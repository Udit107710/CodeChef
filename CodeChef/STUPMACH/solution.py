from sys import stdin, stdout
t = int(stdin.readline())
# for _ in range(t):
#     n = stdin.readline()
#     boxes = list(map(int, stdin.readline().split()))
#     l = -1
#     length = len(boxes)
#     t = length
#     count = 0
#     while t > 0:
#         for index in range(t):
#             if boxes[index] <= 0:
#                 t = index
#                 break
#             else:
#                 boxes[index] -= 1
#                 count+=1
#     print(count)

for _ in range(t):
    n = stdin.readline()
    boxes = list(map(int, stdin.readline().split()))
    length = len(boxes)

    differences = [0] * length
    differences[0] = boxes[0]

    for index in range(1, length):
        differences[index] = min(differences[index-1], boxes[index])
    
    prev = differences[-1]
    count_ = length * prev
    for index in range(length-2, -1, -1):
        if prev == differences[index]:
            continue
        else:
            count_ += ((index+1) * (differences[index] - prev))
            prev = differences[index]
    
    print(count_)