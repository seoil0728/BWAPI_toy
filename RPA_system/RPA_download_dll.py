import requests
import os


def get_bot_binary_by_name(bot_name):
    responce = requests.get('https://sscaitournament.com/api/bots.php?bot={}'.format(bot_name))

    re_dic = responce.json()
    return re_dic[0]


def download_file(url, file_name):
    with open(file_name, "wb") as file:
        responce = requests.get(url)
        file.write(responce.content)


def main():
    if not os.path.isdir('bot_download'):
        os.mkdir('bot_download')
    print('DLL Download')
    while True:
        bot = input('Type bot name (if you want to finish, Just Enter) : ')
        if bot == '':
            break

        bot_dic = get_bot_binary_by_name(bot)
        download_file(bot_dic['bwapiDLL'], 'bot_download/{}.dll'.format(bot_dic['name']))
        print('Download Success!')
        print()


if __name__ == '__main__':
    main()
