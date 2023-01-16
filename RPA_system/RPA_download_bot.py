import datetime
import requests
import os


def get_date():
    date = datetime.datetime.now()
    print(date.strftime('%Y-%m-%d %H:%M:%S'))

    return date.strftime('%Y-%m-%d %H:%M:%S')


def get_bot_binary_by_name(bot_name):
    responce = requests.get('https://sscaitournament.com/api/bots.php?bot={}'.format(bot_name))

    re_dic = responce.json()
    return re_dic[0]


def get_bot_binary_all():
    responce = requests.get('https://sscaitournament.com/api/bots.php')
    re_dic = responce.json()
    return re_dic


def get_updated_log():
    if not os.path.isdir('bot_download'):
        return

    f = open('bot_download/download_log.txt', 'r')

    date = f.read()
    f.close()
    return date


def write_log():
    if not os.path.isdir('bot_download'):
        os.mkdir('bot_download')
    f = open('bot_download/download_log.txt', 'w')
    f.write(get_date())
    f.close()


def initialize_log():
    if not os.path.isdir('bot_download'):
        os.mkdir('bot_download')
    f = open('bot_download/download_log.txt', 'w')
    f.write('2000-01-01 01:00:00')
    f.close()


def download_file(url, file_name):
    with open(file_name, "wb") as file:
        responce = requests.get(url)
        file.write(responce.content)


def main():
    ch = input('If this is first time, Type 1 : ')
    if ch == '1':
        initialize_log()
    updated = get_updated_log()

    bots = get_bot_binary_all()
    for i in bots:
        if i['update'] > updated:
            download_file(i['botBinary'], 'bot_download/{}.zip'.format(i['name']))
            print('updated {} file.'.format(i['name']))

    print()
    print('Update Finished!')
    write_log()


if __name__ == '__main__':
    main()
