a = []
line = input()
p = True
while p:
    try:
        a.append(int(line))
        line = input()
    except:
        p = False 

a = list(map(int, a))

ans = 0
for element in a:
    if element%12 == 0:
        print(element + int(element/12))
    else:
        print(element)