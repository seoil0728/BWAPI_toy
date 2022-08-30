import os


def pushing(player_list):
    if not os.path.exists('draws'):
        os.mkdir("draws")

    os.chdir("draws")

    for i in range(len(player_list)):
        if i < 9:
            os.mkdir("0{} - {} vs {}".format(i + 1, player_list[i][0], player_list[i][1]))
        else:
            os.mkdir("{} - {} vs {}".format(i + 1, player_list[i][0], player_list[i][1]))


def make_draws():
    draws = []
    temp = []

    while True:
        plays = input('Add Player Name (if quit, Just Enter) : ')
        if plays == '':
            break
        else:
            temp.append(plays)

    for i in range(len(temp) // 2):
        dd = []
        dd.append(temp.pop(0))
        dd.append(temp.pop(0))
        draws.append(dd)

    return draws


def main():
    plist = make_draws()
    pushing(plist)


if __name__ == '__main__':
    main()
