T = int(input())

for _ in range(T):
    win_team = {}

    for __ in range(12):
        match = input().split('vs.')
        
        team_1 = str(match[0].split()[0])
        goal_1 = int(match[0].split()[-1])
        
        team_2 = str(match[1].split()[1])
        goal_2 = int(match[1].split()[0])
        
        differ = abs(goal_1 - goal_2)
        if goal_1 > goal_2:
            try:
                win_team[team_1][0] += 3
                win_team[team_1][1] += differ
            except:
                win_team[team_1] = [3, differ]
            try:
                win_team[team_2][1] -= differ
            except:
                win_team[team_2] = [0, -differ]

        elif goal_2 > goal_1:
            try:
                win_team[team_2][0] += 3
                win_team[team_2][1] += differ
            except :
                win_team[team_2] = [3, differ]
            try:
                win_team[team_1][1] -= differ
            except :
                win_team[team_1] = [0, -differ]
        else:
            try:
                win_team[team_1][0] += 1
            except :
                win_team[team_1] = [1, 0]
            try:
                win_team[team_2][0] += 1
            except :
                win_team[team_2] = [1, 0]

    top = ['temp', [-1, -1]]
    top_2 = ['temp', [-1, -1]]
    for key, value in win_team.items():
        if value[0] > top[1][0]:
            temp = top.copy()
            top[0] = key
            top[1] = value
            top_2 = temp
        elif value[0] == top[1][0] and value[1] > top[1][1]:
            temp = top.copy()
            top[0] = key
            top[1] = value
            top_2 = temp
        elif value[0] > top_2[1][0]:
            top_2[0] = key
            top_2[1] = value
        elif value[0] == top_2[1][0] and value[1] > top_2[1][1]:
            top_2[0] = key
            top_2[1] = value
        

    print(top[0], top_2[0])