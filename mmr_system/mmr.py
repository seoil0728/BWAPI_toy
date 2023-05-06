def get_player():
    player_list = []
    with open('./mmr.txt', 'r') as f:
        c = f.read()
        cs = c.split('\n')

        for i in cs:
            if i == '':
                pass
            else:
                player_list.append(i.split('&')[0])

    return player_list


def adding_player():
    player_list = get_player()
    with open('./mmr.txt', 'a') as f:
        while True:
            user = input('Type User name. Initial MMR is 2000 : ')
            if user == '':
                break
            else:
                if user not in player_list:
                    f.write(user + '&' + '2000\n')
                else:
                    print('Already exists.')


def main():
    adding_player()


if __name__ == '__main__':
    main()
