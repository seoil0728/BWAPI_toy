import random
import psl_adding_directory
import psl_round_maker
import psl_map_adviser
import psl_check_pro_title


def make_pre_league():
    player_list = []

    with open('./submit_bots.txt', 'r') as f:
        c = f.read()
        cs = c.split('\n')

        for i in cs:
            if i == '':
                pass
            else:
                player_list.append(i)

    print('Participant =', len(player_list))
    print('additional blank player =', len(player_list) % 4)
    print()

    if len(player_list) % 4 != 0:
        temp = len(player_list) % 4
        for i in range(temp):
            player_list.append('')

    random.shuffle(player_list)

    draws = []

    for i in range(len(player_list)//2):
        temp = []
        temp.append(player_list.pop())
        temp.append(player_list.pop())
        draws.append(temp)
        print(temp)

    destination = input('If you want to make draws folder? (y/n) : ')
    if destination == 'y':
        psl_adding_directory.pushing(draws)


def main():
    print('========== Welcome to the Personal Star-League! ==========')
    print('********************** Command List **********************')
    print('1 : Make Pre-League list (need to update submit_bots.txt)')
    print('2 : Make Round List')
    print('3 : Make Draws Directories (01 - A vs B Format)')
    print('4 : PSL Map Adviser (RO16, RO8, Semi-Final, Final')
    print('5 : PSL Pro-gamer List (3-Season update)')
    print('**********************************************************')
    command = input('What do you want to do? : ')
    print()

    if command == '1':
        make_pre_league()
    elif command == '2':
        print('1: Make 16 Round.')
        print('2: Make 8 Round.')
        print('3: Make 4 Round.')
        command = input('What do you want to do? : ')
        if command == '1':
            psl_round_maker.make_16_round()
        elif command == '2':
            psl_round_maker.make_8_round()
        elif command == '3':
            psl_round_maker.make_4_round()
        else:
            print('Invalid Command.')
    elif command == '3':
        p_list = psl_adding_directory.make_draws()
        psl_adding_directory.pushing(p_list)
    elif command == '4':
        map_list = ['Benzene', 'Destination', 'Heartbreak Ridge', 'Neo Moon Glave', 'Tau Cross', 'Andromeda',
                    'Circuit Breaker', 'Electric Circuit', 'Empire of the Sun', 'Fighting Spirit', 'Icarus', 'Jade',
                    'La Mancha', 'Python', 'Road Runner']
        psl_map_adviser.map_advice(map_list)
    elif command == '5':
        psl_check_pro_title.check_pro()
    else:
        print('Invalid Command!')


if __name__ == '__main__':
    main()
