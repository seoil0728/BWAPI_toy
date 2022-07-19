import random

ls = []

while True:
    answer = input('Type : ')
    if answer == '':
        break
    else:
        ls.append(answer)

# random.shuffle(ls)
# random.shuffle(ls)
# random.shuffle(ls)
# random.shuffle(ls)
#
# print()
# for i in ls:
#     print(i)
#


a = random.randint(0, len(ls))

print(ls[a])
