import os
import shutil
from distutils.dir_util import copy_tree


def remove_files():
    try:
        shutil.rmtree(".")
    except Exception as e:
        print(e)


def find_directory():
    name = input('Type bot name: ')
    for i in os.listdir():
        if name in i:
            name = i
            break

    return name


os.chdir("C:/Starcraft/bwapi-data/AI")
remove_files()

os.chdir("D:/bwapi/bot/")
directories = find_directory() + '/a'
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

