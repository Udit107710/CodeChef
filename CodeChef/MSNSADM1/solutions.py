T = int(input())
for _ in range(T):
    players = int(input())
    goals = map(int,input().split())
    penalties = map(int, input().split())
    
    score = lambda x: x*20
    foul = lambda x: x*-10
    
    max_point = -500

    score_goals = list(map(score, goals))
    foul_penalties = list(map(foul, penalties))

    for i in range(players):
        player = score_goals[i] + foul_penalties[i]
        if player > max_point:
            max_point = player
    if max_point >= 0:
        print(max_point)
    else:
        print(0)