def distance(A, B):
    return ((B[0]-A[0])**2 + (B[1]-A[1])**2)**0.5


for _ in range(int(input())):
    n, q = map(int, input().split())
    points = list(map(int, input().split()))
    for __ in range(q):
        x1, x2, y = map(int, input().split())
        count = 0
        for i in range(n-1):
            point1 = (i+1, points[i])
            point2 = (i+2, points[i+1])
            if i+1 > x1 and i+1 < x2 and i+2 < x2 and i+2 > x1 and ( (points[i+1] <= y and points[i] >= y) or (points[i] <= y and points[i+1] >= y) ) :
                count+=1
            elif (x2 == i+1 and y == points[i]) or (x1 == i+2 and y == points[i+1]):
                continue
            else:
                A1 = points[i+1] - points[i]
                B1 = -1
                C1 = A1*(i+1) + B1*points[i]
                A2 = 0
                B2 = x2-x1
                C2 = B2*y

                det = A1*B2 - A2*B1
                if det == 0:
                    continue
                else:
                    x = (B2*C1 - B1*C2)/det
                    yf = (A1*C2 - A2*C1)/det
                    if x >= x1 and x <= x2 and y==yf and (distance([i+1, points[i]], [x, yf]) + distance([x, yf], [i+2, points[i+1]]) == distance([i+1, points[i]], [i+2, points[i+1]])):
                        count+=1
        print(count)