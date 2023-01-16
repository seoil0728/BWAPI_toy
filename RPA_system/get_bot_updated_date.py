import requests


def get_bot_binary_by_name(bot_name):
    responce = requests.get('https://sscaitournament.com/api/bots.php?bot={}'.format(bot_name))

    re_dic = responce.json()
    return re_dic[0]


def get_bot_binary_all():
    responce = requests.get('https://sscaitournament.com/api/bots.php')
    re_dic = responce.json()
    return re_dic


def main():
    ch = input('Check all bots update? Type 1 : ')
    if ch == '1':
        bots = get_bot_binary_all()
        update_list = []
        for bot in bots:
            update_list.append((bot['update'], bot['name'], bot['race']))

        update_list.sort()
        for i in update_list:
            print(i)

    else:
        while True:
            bot_name = input('Type bot name, Just Enter to Finish : ')
            if bot_name == '':
                break
            bot = get_bot_binary_by_name(bot_name)
            print((bot['update'], bot['name'], bot['race']))


if __name__ == '__main__':
    main()
