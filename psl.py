import random

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

temp = []
for i in range(len(player_list)//2):
    temp.append(player_list.pop())
    temp.append(player_list.pop())
    print(temp)
    temp.clear()


