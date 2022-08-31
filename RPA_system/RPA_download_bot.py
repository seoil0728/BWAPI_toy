from bs4 import BeautifulSoup
import requests
import time
import os


def get_pages():
    response = requests.get('https://sscaitournament.com/index.php?action=scores')

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.find_all('td', class_='bot_updated')
        for tags in title:
            print(tags.get_text())

    else:
        print(response.status_code)


def get_today():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


def check_updated():
    print(os.getcwd())
    if not os.path.isdir('bot_download'):
        os.mkdir('bot_download')

    os.chdir('bot_download')
    today_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

    if not os.path.isdir(today_date):
        os.mkdir(today_date)


def main():
    check_updated()
    get_today()
    get_pages()


if __name__ == '__main__':
    main()
