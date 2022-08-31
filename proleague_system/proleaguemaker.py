import random


def make_team(num_member):
    team1 = []
    team2 = []

    selection = input('1. Random Choice, 2. Sequence Choice : ')

    if selection == '1':
        for i in range(num_member):
            member = input('Type Member : ')
            team1.append(member)

        random.shuffle(team1)

        for i in range(int(num_member / 2)):
            team2.append(team1.pop())
    else:
        for i in range(num_member // 2):
            member = input('Type Team 1 Member : ')
            team1.append(member)
        for i in range(num_member // 2):
            member = input('Type Team 2 Member : ')
            team2.append(member)

    return team1, team2


def main():
    team1, team2 = make_team(8)
    print(team1)
    print(team2)


if __name__ == '__main__':
    main()
