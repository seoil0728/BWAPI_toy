import random


def make_team(num_member):
    team1 = []
    team2 = []

    for i in range(num_member):
        member = input('Type Member : ')
        team1.append(member)

    random.shuffle(team1)

    for i in range(int(num_member / 2)):
        team2.append(team1.pop())

    return team1, team2


def main():
    team1 , team2 = make_team(8)
    print(team1)
    print(team2)


if __name__ == '__main__':
    main()
