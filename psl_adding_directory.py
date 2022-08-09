import os


def pushing(player_list):
    if not os.path.exists('draws'):
        os.mkdir("draws")

    os.chdir("draws")

    for i in range(len(player_list)):
        if i < 10:
            os.mkdir("0{} - {} vs {}".format(i + 1, player_list[i][0], player_list[i][1]))
        else:
            os.mkdir("{} - {} vs {}".format(i + 1, player_list[i][0], player_list[i][1]))


def main():
    plist = [["Volas", "Stardust"], ["Test", "Test2"]]
    pushing(plist)


if __name__ == '__main__':
    main()
