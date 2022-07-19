team1 = []
team2 = []
team1_set_score = 0
team2_set_score = 0

num_member = int(input('Type whole Number of Members : '))

for i in range(num_member):
    member = input('Type Team Member (Team1 First) : ')
    if i < num_member/2:
        team1.append(member)
    else:
        team2.append(member)

print()

print('1set ProLeague!')
print()
set_count = 0
team1_win = 0
team2_win = 0

while set_count < 7:
    if set_count > 3:
        team1_member = input('Who run? (team1) : ')
        team2_member = input('Who run? (team2) : ')
    else:
        team1_member = team1[set_count]
        team2_member = team2[set_count]

    print(set_count + 1, 'set', team1_member, 'vs', team2_member)
    win_team = int(input('Whose team win? (1 or 2) : '))
    if win_team == 1:
        team1_win += 1
    else:
        team2_win += 1

    if team1_win == 4 or team2_win == 4:
        print('Well Done, Proleague is Done!')
        break
    else:
        print("OK, We'll gonna next match up")
        set_count += 1

if team1_win == 4:
    print('1Set ProLeague Winner is Team1!', team1_win, 'vs', team2_win)
    team1_set_score += 1
else:
    print('1Set ProLeague Winner is Team2!', team1_win, 'vs', team2_win)
    team2_set_score += 1

print()

print('2set WinnersLeague!')
print()
set_count = 0
team1_win = 0
team2_win = 0
last_win = 0
temp = ''

while set_count < 7:
    if last_win == 0:
        team1_member = input('Who run? (team1) : ')
        team2_member = input('Who run? (team2) : ')
    else:
        if last_win == 1:
            team1_member = temp
            team2_member = input('Who run? (team2) : ')
        else:
            team1_member = input('Who run? (team1) : ')
            team2_member = temp

    print(set_count + 1, 'set', team1_member, 'vs', team2_member)
    win_team = int(input('Whose team win? (1 or 2) : '))
    if win_team == 1:
        team1_win += 1
        last_win = 1
        temp = team1_member
    else:
        team2_win += 1
        last_win = 2
        temp = team2_member

    if team1_win == 4 or team2_win == 4:
        print('Well Done, Proleague is Done!')
        break
    else:
        print("OK, We'll gonna next match up")
        set_count += 1

if team1_win == 4:
    print('2Set WinnersLeague Winner is Team1!', team1_win, 'vs', team2_win)
    team1_set_score += 1
else:
    print('2Set WinnersLeague Winner is Team2!', team1_win, 'vs', team2_win)
    team2_set_score += 1

print()

if team1_set_score == team2_set_score:
    print('3set Super Ace Match!')
    team1_member = input('Who run? : ')
    team2_member = input('Who run? : ')
    win_team = int(input('Whose team win? (1 or 2) : '))

    if win_team == 1:
        team1_set_score += 1
    else:
        team2_set_score += 1

print()
print('ProLeague is Done! The Winner Team is,')
if team1_set_score == 2:
    print('Team 1 ! Congratulation!')
else:
    print('Team 2 ! Congratulation')
