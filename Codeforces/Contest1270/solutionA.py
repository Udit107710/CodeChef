from sys import stdin, stdout

t = int(stdin.readline())
for _ in range(t):
    count_all, count_one, count_two = map(int, stdin.readline().split())
    player_one = list(map(int, stdin.readline().split()))
    player_two = list(map(int, stdin.readline().split()))

    player_win = max(player_one) > max(player_two)

    if player_win:
        print('YES')
    else:
        print('NO')
