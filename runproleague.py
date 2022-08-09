import proleaguemaker
import randompop
import copy


def main():
    team1 = []
    team2 = []
    team1_set_score = 0
    team2_set_score = 0

    num_member = int(input('Type whole Number of Members : '))

    team1, team2 = proleaguemaker.make_team(num_member)
    print('Team 1 :', team1)
    print('Team 2 :', team2)

    print()

    print('1set ProLeague!')
    print()
    set_count = 0
    team1_win = 0
    team2_win = 0

    while set_count < num_member - 1:
        if set_count > (num_member / 2) - 1:
            team1_member = randompop.choose_random(team1)
            team2_member = randompop.choose_random(team2)
        else:
            team1_member = team1[set_count]
            team2_member = team2[set_count]

        print(set_count + 1, 'set', team1_member, 'vs', team2_member)
        win_team = int(input('Whose team win? (1 or 2) : '))
        if win_team == 1:
            team1_win += 1
        else:
            team2_win += 1

        if team1_win == (num_member / 2) or team2_win == (num_member / 2):
            print('Well Done, Proleague is Done!')
            break
        else:
            print("OK, We'll gonna next match up")
            set_count += 1

    if team1_win == (num_member / 2):
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
    team1_temp = copy.deepcopy(team1)
    team2_temp = copy.deepcopy(team2)
    temp = ''

    while set_count < num_member - 1:
        if last_win == 0:
            team1_member = randompop.choose_random(team1_temp)
            team2_member = randompop.choose_random(team2_temp)
            team1_temp.remove(team1_member)
            team2_temp.remove(team2_member)
        else:
            if last_win == 1:
                team1_member = temp
                team2_member = randompop.choose_random(team2_temp)
                team2_temp.remove(team2_member)
            else:
                team1_member = randompop.choose_random(team1_temp)
                team1_temp.remove(team1_member)
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

        if team1_win == (num_member / 2) or team2_win == (num_member / 2):
            print('Well Done, Proleague is Done!')
            break
        else:
            print("OK, We'll gonna next match up")
            set_count += 1

    if team1_win == (num_member / 2):
        print('2Set WinnersLeague Winner is Team1!', team1_win, 'vs', team2_win)
        team1_set_score += 1
    else:
        print('2Set WinnersLeague Winner is Team2!', team1_win, 'vs', team2_win)
        team2_set_score += 1

    print()

    if team1_set_score == team2_set_score:
        print('3set Super Ace Match!')
        team1_member = randompop.choose_random(team1)
        team2_member = randompop.choose_random(team2)
        print(team1_member, 'vs', team2_member)
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


if __name__ == '__main__':
    main()

