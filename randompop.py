import random

def choose_random(team):
    random.shuffle(team)
    random.shuffle(team)
    return team[0]


def main():
    team = ["Stardust", "Volas", "Monster", "adias"]
    print(choose_random(team))


if __name__ == '__main__':
    main()
