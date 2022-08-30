# with open('./resource/contents1.txt', 'a') as f:
#     f.write('I love python2\n')


with open('./users.txt', 'w') as f:
    typing = True

    while typing:
        user = input('Type users name, Better player first (if end, type exit) : ')
        if user == 'exit':
            typing = False

        else:
            f.write(user + '&')

print('Adding User is Complete!')
