import random
import psl_adding_directory

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

psl_adding_directory.pushing(draws)
