import random
player_list = []
map_list = ['Benzene', 'Destination', 'Heartbreak Ridge', 'Neo Moon Glave', 'Tau Cross', 'Andromeda',
            'Circuit Breaker', 'Electric Circuit', 'Empire of the Sun', 'Fighting Spirit', 'Icarus', 'Jade',
            'La Mancha', 'Python', 'Road Runner']

with open('./mmr.txt', 'r') as f:
    c = f.read()
    cs = c.split('\n')

    for i in cs:
        if i == '':
            pass
        else:
            player_list.append(i)

a = random.randrange(len(player_list))
b = random.randrange(len(player_list))

print('{} versus {} !'.format(player_list[a], player_list[b]))
print('Map is {}'.format(map_list[random.randrange(len(map_list))]))
