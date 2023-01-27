import os
import subprocess


def detect_bot(bot_name):
    exe_bot = ['adias', 'Bereaver', 'Boris', 'DTD Bot', 'JJJJJ', 'krasi0', 'Monster', 'MicRobot', 'Pathos', 'Pinfel 2',
               'Prism Cactus', 'StyxZ2', 'Sune Rasmussen', 'tscmoo', 'Zerg Hell']
    jar_bot = ['Delingvery', 'Ecgberht', 'Fifou Legend', 'ForceBot', 'Hopark', 'Infested Artosis', 'KangarooBot',
               'KaonBot', 'Marine Hell', 'MadMix', 'PurpleWave', 'Simplicity', 'Slater', 'Soeren Klett', 'StyxZ',
               'Tomas Cere', 'TyrProtoss', 'WillBot', 'Zealot Hell', 'ZurZurZur']

    for i in exe_bot:
        if i in bot_name:
            run_bat(i)

    for i in jar_bot:
        if i in bot_name:
            run_jar()


def run_jar():
    directory = os.getcwd().replace('\\', '/') + '/run_bat_file/'
    bot = directory + 'runjava.bat'
    subprocess.call([bot])


def run_bat(bot):
    directory = os.getcwd().replace('\\', '/') + '/run_bat_file/'

    if bot == 'adias':
        bot = directory + 'runadias.bat'
    if bot == 'Bereaver':
        bot = directory + 'runBereaver.bat'
    if bot == 'Boris':
        bot = directory + 'runBoris.bat'
    if bot == 'DTD Bot':
        bot = directory + 'runDTDBot.bat'
    if bot == 'JJJJJ':
        bot = directory + 'runJJJJJ.bat'
    if bot == 'krasi0':
        bot = directory + 'runkrasi0.bat'
    if bot == 'MicRobot':
        bot = directory + 'runMicRobot.bat'
    if bot == 'Monster':
        bot = directory + 'runMonster.bat'
    if bot == 'Pathos':
        bot = directory + 'runPathos.bat'
    if bot == 'Pinfel 2':
        bot = directory + 'runPinfel.bat'
    if bot == 'Prism Cactus':
        bot = directory + 'runPrismCactus.bat'
    if bot == 'StyxZ2':
        bot = directory + 'runStyxZ2.bat'
    if bot == 'Sune Rasmussen':
        bot = directory + 'runSuneR.bat'
    if bot == 'tscmoo':
        bot = directory + 'runtscmoo.bat'
    if bot == 'Zerg Hell':
        bot = directory + 'runZergHell.bat'

    subprocess.call([bot])


def main():
    detect_bot('BetaStar')


if __name__ == '__main__':
    main()
