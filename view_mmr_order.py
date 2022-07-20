import time

player_list = []

print('Ordered MMR List')
print()

with open('./mmr.txt', 'r') as f:
    c = f.read()
    cs = c.split('\n')

    for i in cs:
        if i == '':
            pass
        else:
            a = i.split(' ')
            a.reverse()
            sts = a[0] + ' ' + a[1]
            player_list.append(sts)

player_list.sort()
player_list.reverse()
rank = 0

tm = time.localtime(time.time())
file_name = 'mmr/' + str(tm.tm_year) + '_' + str(tm.tm_mon) + '_' + str(tm.tm_mday) + '_MMR Rank.txt'
with open(file_name, 'w') as f:
    for i in player_list:
        rank += 1
        a = i.split(' ')
        a.reverse()
        sts = a[0] + ' ' + a[1]
        print(str(rank) + '. ' + sts)
        f.write(str(rank) + '. ' + sts + '\n')
