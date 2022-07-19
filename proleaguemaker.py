import random

team1 = []
team2 = []

while True:
    answer = input('Type User Name (if finished, just enter) : ')
    if answer == '':
        break
    else:
        team1.append(answer)

random.shuffle(team1)
a = int(len(team1)/2)

for i in range(a):
    team2.append(team1.pop())

print(team1)
print(team2)
