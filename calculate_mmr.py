def mmr_calculate(a, b):
    if a < b:
        a, b = b, a

    weight = (a - b)

    if weight < 500:
        weight *= 0.2
    else:
        weight = 99
    print('Weight is', int(weight))
    return weight


def mmr_by_player(player_list, player_a, player_b):
    i = 0
    mmr_a = 0
    mmr_b = 0
    while True:
        if player_a in player_list[i]:
            mmr_a = int(player_list[i][1])
            break
        else:
            if i == len(player_list):
                break
            else:
                i += 1

    i = 0
    while True:
        if player_b in player_list[i]:
            mmr_b = int(player_list[i][1])
            break
        else:
            if i == len(player_list):
                break
            else:
                i += 1

    print(player_a + ' mmr =', mmr_a)
    print(player_b + ' mmr =', mmr_b)

    weight = mmr_calculate(mmr_a, mmr_b)
    return weight


def print_mmr(mmr, weight):
    print('Need to Add/Subtract mmr is {} +- {}.'.format(mmr, weight))
    print('Upper Win = {}, Lose = {}'.format(mmr - weight, mmr + weight))
    print('Lower Win = {}, Lose = {}'.format(mmr + weight, mmr - weight))


def is_upper(a, b):
    return a >= b


def main():
    player_list = []

    with open('./mmr.txt', 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            line = line.strip()
            line = line.split('&')
            player_list.append(line)

    order = input('1. by Name, 2. by mmr : ')

    if order == '1':
        a = input('Type A Name : ')
        b = input('Type B Name : ')

        mmr = 100
        weight = mmr_by_player(player_list, a, b)

        print_mmr(mmr, weight)

    else:
        a = int(input('Type A mmr : '))
        b = int(input('Type B mmr : '))

        mmr = 100
        weight = mmr_calculate(a, b)
        print_mmr(mmr, weight)


if __name__ == '__main__':
    main()
