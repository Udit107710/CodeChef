from sys import stdin, stdout

T = int(stdin.readline())

for _ in range(T):
    string = input()
    count = 0
    prev = string[0]
    new_string = ''
    length = 0

    for value in string:
        length +=1
        if value == prev:
            count+=1
        else:
            new_string += prev + str(count)
            prev = value
            count = 1
    new_string+=prev + str(count)
    # print(new_string, len(new_string), string, len(string), length)

    if len(new_string) < len(string):
        print('YES')
    else:
        print('NO')