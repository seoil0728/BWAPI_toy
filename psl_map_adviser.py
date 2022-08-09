import random


def map_advice(map_list):
    print('RO16 Map Adviser :', random.sample(map_list, 3))
    print('RO8 Map Adviser :', random.sample(map_list, 5))
    print('Semi-Final Map Adviser :', random.sample(map_list, 5))
    print('Final Map Adviser :', random.sample(map_list, 5))


def main():
    map_list = ['Benzene', 'Destination', 'Heartbreak Ridge', 'Neo Moon Glave', 'Tau Cross', 'Andromeda',
                'Circuit Breaker', 'Electric Circuit', 'Empire of the Sun', 'Fighting Spirit', 'Icarus', 'Jade',
                'La Mancha', 'Python', 'Road Runner']
    map_advice(map_list)


if __name__ == '__main__':
    main()
