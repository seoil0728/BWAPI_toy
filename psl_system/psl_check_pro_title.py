from collections import Counter


def check_pro():
    progamers = dict()
    checker1 = Counter()
    checker2 = Counter()
    checker3 = Counter()

    progamers[1] = [['adias', 'Monster', 'Volas', 'BananaBrain', 'krasi0', 'Dragon', 'Stardust', 'Crona'],
                    ['Proxy', 'DaQin', 'Iron bot', 'Locutus', 'McRave', 'Microwave', 'WillyT', 'PurpleWave']]

    progamers[2] = [['Volas', 'adias', 'Stardust', 'BananaBrain', 'ZNZZBot', 'Monster', 'Halo', 'Iron bot'],
                    ['Microwave', 'Killerbot', 'krasi0P', 'WillyT', 'Hao Pan', 'DaQin', 'LetaBot', 'legacy']]

    progamers[3] = [['Stardust', 'DaQin', 'Monster', 'BananaBrain', 'Hao Pan', 'ZNZZBot', 'BetaStar', 'Brainiac'],
                    ['Chris Coxe', 'adias', 'Dragon', 'krasi0', 'WuliBot', 'McRaveZ', 'PurpleWave', 'krasi0P']]

    progamers[4] = [['Volas', 'Stardust', 'adias', 'Monster', 'Killerbot', 'BananaBrain', 'DaQin', 'XIAOYICOG2019'],
                    ['Zia bot', 'NLPRbot', 'ZNZZBot', 'Iron bot', 'Brainiac', 'Crona', 'legacy', 'Dave Churchill']]

    progamers[5] = [['Volas', 'Monster', 'Stardust', 'Brainiac', 'adias', 'BananaBrain', 'Dragon', 'krasi0'],
                    ['Killerbot', 'Halo', 'ZNZZBot', 'Iron bot', 'WillyT', 'NiteKatT', 'skyFORKnet', 'BetaStar']]

    checker1 = progamers[len(progamers)][0]
    checker2 = progamers[len(progamers) - 1][0]
    checker3 = progamers[len(progamers) - 2][0]

    major = Counter(checker1 + checker2 + checker3)
    print('Current Major Progamer list!')
    print(list(major))
    print()

    checker1 = progamers[len(progamers)][1]
    checker2 = progamers[len(progamers) - 1][1]
    checker3 = progamers[len(progamers) - 2][1]

    k_league = Counter(checker1 + checker2 + checker3)
    print('Current K-League Progamer list!')
    print(list(k_league - major))
    print()

    ex_pro = set()
    for i in range(len(progamers)):
        ex_pro.update(progamers[i + 1][0])
        ex_pro.update(progamers[i + 1][1])

    checker1 = Counter(list(ex_pro))

    print('Ex_Progamer list!')
    print(list(checker1 - major - k_league))


def main():
    check_pro()


if __name__ == '__main__':
    main()
