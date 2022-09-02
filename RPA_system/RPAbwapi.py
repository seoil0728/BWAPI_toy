import os
import shutil
from distutils.dir_util import copy_tree
import RPArunchaos
import RPArunbot


def remove_files():
    try:
        shutil.rmtree(".")
    except Exception as e:
        print(e)


def find_directory():
    detected = []
    name = input('Type bot name: ')
    for i in os.listdir():
        if name in i:
            detected.append(i)

    return detected


def main():
    original_cwd = os.getcwd()
    # delete past bwapi files in bwapi-data/AI
    os.chdir("C:/Starcraft/bwapi-data/AI")
    remove_files()

    # Find bot by name
    os.chdir("D:/bwapi/bot/")
    founded = find_directory()

    # check bots, if searched files are not just one, give a selection
    if len(founded) == 1:
        directories = founded[0] + '/a'
    elif len(founded) > 1:
        print('Multiple Founded. need selection')
        for index in range(len(founded)):
            print('{} : {}'.format(index + 1, founded[index]))
        selection = int(input('What you want? : '))
        directories = founded[selection-1] + '/a'
    else:
        directories = 'not found'

    # if not founded, just exit code
    if directories == 'not found':
        print('Not Founded. Check bots name.')

    # if founded, try to copy files
    else:
        os.chdir(directories)

        files_and_folders = os.listdir()
        for i in files_and_folders:
            if os.path.isdir(i):
                try:
                    copy_tree(i, 'C:/Starcraft/bwapi-data/AI/' + i)
                except Exception as e:
                    print(e)

        try:
            for root, dirs, files in os.walk("."):
                for file_name in files:
                    shutil.copy2(file_name, 'C:/Starcraft/bwapi-data/AI')
            print('Copied!')
        except Exception as e:
            print(e)

        os.chdir('C:/Starcraft/bwapi-data')
        try:
            os.remove('BWAPI.dll')
            os.remove('bwapi.ini')
        except Exception as e:
            print(e)

        try:
            shutil.move('AI/BWAPI.dll', '.')
            shutil.move('AI/bwapi.ini', '.')
            print('Process Success!')
        except Exception as e:
            print(e)

        auto_start = input('If you want to start Starcraft Automatically, Type 1 : ')
        if auto_start == '1':
            os.chdir(original_cwd)
            RPArunchaos.main()
            RPArunbot.detect_bot(directories)


if __name__ == '__main__':
    main()
