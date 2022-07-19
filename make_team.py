import random

f = open('./users.txt', 'r', encoding='UTF-8')
c = f.read()

list_of_all_users = c.split('&')
major_player = []
middle_player = []
underdog_player = []

count = 0

for i in list_of_all_users:
    count += 1
    if i == '':
        pass
    else:
        if count < 17:
            major_player.append(i)
        elif count < 33:
            middle_player.append(i)
        else:
            underdog_player.append(i)

random.shuffle(major_player)
random.shuffle(middle_player)
random.shuffle(underdog_player)

print(major_player)
print(middle_player)
print(underdog_player)


print('Major Player :', len(major_player))
print('Middle Player :', len(middle_player))
print('Underdog Player :', len(underdog_player))
