import calculate_mmr


def write_file(player_list):
    with open('./mmr.txt', 'w') as f:
        for i in player_list:
            line = i[0] + ' ' + i[1] + '\n'
            f.write(line)


def load_players():
    players = []

    with open('./mmr.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            line = line.split(' ')
            players.append(line)

    return players


def find_player_mmr(player_list, player_name):
    i = 0
    mmr_s = 0
    while True:
        if player_name in player_list[i]:
            mmr_s = int(player_list[i][1])
            break
        else:
            if i == len(player_list):
                break
            else:
                i += 1
    return mmr_s


def change_mmr(player_list, player_name, mmr):
    i = 0
    while True:
        if player_name in player_list[i]:
            player_list[i][1] = str(int(player_list[i][1]) + mmr)
            print('Updated! Current mmr = {}'.format(player_list[i][1]))
            break
        else:
            if i == len(player_list):
                break
            else:
                i += 1
    return player_list


def win_lose(player_list):
    player_a = input('Type A Name : ')
    player_b = input('Type B Name : ')
    mmr_a = find_player_mmr(player_list, player_a)
    mmr_b = find_player_mmr(player_list, player_b)

    print(player_a + ' mmr =', mmr_a)
    print(player_b + ' mmr =', mmr_b)

    weight = int(calculate_mmr.mmr_calculate(mmr_a, mmr_b))
    mmr = 100
    winner = input('Who win? (1 or 2) : ')

    # Winner is A
    if winner == '1':
        # Upper is A
        if calculate_mmr.is_upper(mmr_a, mmr_b):
            mmr -= weight
            player_list = change_mmr(player_list, player_a, mmr)
            player_list = change_mmr(player_list, player_b, -mmr)
        # Upper is B
        else:
            mmr += weight
            player_list = change_mmr(player_list, player_a, mmr)
            player_list = change_mmr(player_list, player_b, -mmr)

    # Winner is B
    else:
        # Upper is A
        if calculate_mmr.is_upper(mmr_a, mmr_b):
            mmr += weight
            player_list = change_mmr(player_list, player_a, -mmr)
            player_list = change_mmr(player_list, player_b, mmr)
        # Upper is B
        else:
            mmr -= weight
            player_list = change_mmr(player_list, player_a, -mmr)
            player_list = change_mmr(player_list, player_b, mmr)

    return player_list


def change_one_mmr(player_list):
    update_user = input('Type User Name : ')
    for i in player_list:
        if update_user in i:
            print('Current mmr : {}'.format(i[1]))

    mmr = int(input('Type MMR add/subtract : '))

    player_list = change_mmr(player_list, update_user, mmr)
    return player_list


def main():
    player_list = load_players()
    print(player_list)

    orders = input('Win Lose? or Just Update One User? (1 or 2) : ')
    if orders == '1':
        player_list = win_lose(player_list)
        write_file(player_list)
    elif orders == '2':
        player_list = change_one_mmr(player_list)
        write_file(player_list)
    else:
        print('Incorrect Order!')


if __name__ == '__main__':
    main()
