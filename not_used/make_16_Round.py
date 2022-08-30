import random

player_list = []

while True:
    a = input('Add Player Name (if quit, Just Enter) : ')
    if a == '':
        break
    else:
        player_list.append(a)

answer = []
for i in range(8):
    temp = []
    x = random.randrange(len(player_list))
    temp.append(player_list[x])
    player_list.remove(player_list[x])

    y = random.randrange(len(player_list))
    temp.append(player_list[y])
    player_list.remove(player_list[y])

    answer.append(temp)

print(answer)
