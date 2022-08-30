
with open('./mmr.txt', 'a') as f:
    while True:
        user = input('Type User name. Initial MMR is 2000 : ')
        if user == '':
            break
        else:
            f.write(user + '&' + '2000\n')


