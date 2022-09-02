import os
import subprocess


def detect_bot(bot_name):
    exe_bot = ['adias', 'Bereaver', 'JJJJJ', 'krasi0', 'Monster', 'Pathos', 'Prism Cactus', 'tscmoo',
               'Zerg Hell']
    jar_bot = ['Fifou Legend', 'MadMix', 'PurpleWave', 'Simplicity', 'StyxZ', 'Tomas Cere', 'TyrProtoss']

    for i in exe_bot:
        if i in bot_name:
            run_bat(i)

    for i in jar_bot:
        if i in bot_name:
            run_bat(i)


def run_bat(bot):
    directory = os.getcwd().replace('\\', '/') + '/run_bat_file/'
    if bot == 'adias':
        bot = directory + 'runadias.bat'
    if bot == 'Bereaver':
        bot = directory + 'runBereaver.bat'
    if bot == 'JJJJJ':
        bot = directory + 'runJJJJJ.bat'
    if bot == 'krasi0':
        bot = directory + 'runkrasi0.bat'
    if bot == 'Monster':
        bot = directory + 'runMonster.bat'
    if bot == 'Pathos':
        bot = directory + 'runPathos.bat'
    if bot == 'Prism Cactus':
        bot = directory + 'runPrismCactus.bat'
    if bot == 'tscmoo':
        bot = directory + 'runtscmoo.bat'
    if bot == 'Fifou Legend':
        bot = directory + 'runjava.bat'
    if bot == 'MadMix':
        bot = directory + 'runjava.bat'
    if bot == 'PurpleWave':
        bot = directory + 'runjava.bat'
    if bot == 'Simplicity':
        bot = directory + 'runjava.bat'
    if bot == 'StyxZ':
        bot = directory + 'runjava.bat'
    if bot == 'Tomas Cere':
        bot = directory + 'runjava.bat'
    if bot == 'TyrProtoss':
        bot = directory + 'runjava.bat'
    if bot == 'Zerg Hell':
        bot = directory + 'runZergHell.bat'

    subprocess.call([bot])


def main():
    detect_bot('BetaStar')


if __name__ == '__main__':
    main()
