import random


def make_16_round():
    p_list = []

    for i in range(12):
        p_list.append(input('Type Players Name : '))

    random.shuffle(p_list)

    print('Group A')
    print(p_list.pop(0), end=', ')
    print(p_list.pop(0), end=', ')
    print(p_list.pop(0))
    print()

    print('Group B')
    print(p_list.pop(0), end=', ')
    print(p_list.pop(0), end=', ')
    print(p_list.pop(0))
    print()

    print('Group C')
    print(p_list.pop(0), end=', ')
    print(p_list.pop(0), end=', ')
    print(p_list.pop(0))
    print()

    print('Group D')
    print(p_list.pop(0), end=', ')
    print(p_list.pop(0), end=', ')
    print(p_list.pop(0))
    print()


def make_8_round():
    p_list = []

    for i in range(8):
        p_list.append(input('Type Players Name : '))

    random.shuffle(p_list)

    print('Group A')
    print(p_list.pop(0), end=', ')
    print(p_list.pop(0))
    print()

    print('Group B')
    print(p_list.pop(0), end=', ')
    print(p_list.pop(0))
    print()

    print('Group C')
    print(p_list.pop(0), end=', ')
    print(p_list.pop(0))
    print()

    print('Group D')
    print(p_list.pop(0), end=', ')
    print(p_list.pop(0))
    print()


def make_4_round():
    p_list = []

    for i in range(4):
        p_list.append(input('Type Players Name : '))

    random.shuffle(p_list)

    print('Group A')
    print(p_list.pop(0), end=', ')
    print(p_list.pop(0))
    print()

    print('Group B')
    print(p_list.pop(0), end=', ')
    print(p_list.pop(0))
    print()


def main():
    make_8_round()


if __name__ == '__main__':
    main()
