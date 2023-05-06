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
            player_list.append(i.replace('&', ' '))

a = random.randrange(len(player_list))
b = random.randrange(len(player_list))

print('{} versus {} !'.format(player_list[a], player_list[b]))
print('Map is {}'.format(map_list[random.randrange(len(map_list))]))

with open('./1 vs 1 Match.txt', 'a') as f:
    f.write('{} versus {} !'.format(player_list[a], player_list[b]))
    f.write('\n')
    f.write('Map is {}'.format(map_list[random.randrange(len(map_list))]))
    f.write('\n\n')

