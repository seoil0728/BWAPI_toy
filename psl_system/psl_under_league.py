import random


def make_under_league():
    p_list = []

    while True:
        bot = input('Add Player Name (if quit, Just Enter) : ')
        if bot == '':
            break
        else:
            p_list.append(bot)

    random.shuffle(p_list)
    capacity = input('How many players? : ')

    try:
        capacity = int(capacity)
        if capacity >= len(p_list):
            for i in p_list:
                print(i)
        else:
            for i in range(capacity):
                print(p_list.pop())
    except:
        print('Invalid data Type')


def main():
    make_under_league()


if __name__ == '__main__':
    main()
