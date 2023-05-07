from pywinauto import application
import pywinauto
import os


def get_chaos_directory():
    path = "C:/"
    chaos_list = []

    for file in os.walk(path):
        if 'Chaoslauncher - MultiInstance.exe' in file[2]:
            chaos_path = file[0] + '/' + file[2][0]
            chaos_list.append(chaos_path.replace('\\', '/'))

    if len(chaos_list) == 1:
        return chaos_list[0]
    else:
        for i, file in enumerate(chaos_list):
            print("{} : {}".format(i, file))
        choice = input('Which one is right? : ')
        try:
            return chaos_list[int(choice)]
        except Exception as e:
            print(e)
            return ''


def save_chaos_path(path):
    if path == '':
        print('There is no Chaoslauncher')
        return 'C:/'

    with open('./chaospath.tmp', 'w') as f:
        f.write(path)


def run_chaos():
    if os.path.isfile('./chaospath.tmp'):
        with open('./chaospath.tmp', 'r') as f:
            chaos = f.read()
    else:
        chaos = get_chaos_directory()
        save_chaos_path(chaos)

    app = application.Application(backend='uia')
    app.start(chaos)


def check_run_chaos():
    processes = pywinauto.findwindows.find_elements()
    for proc in processes:
        if proc.name == 'Chaoslauncher':
            print('Chaos Launcher is already running.')
            return True
    return False


def run_starcraft_from_chaos():
    app = application.Application(backend='uia')
    processes = pywinauto.findwindows.find_elements()
    for proc in processes:
        if proc.name == 'Chaoslauncher':
            app.connect(process=proc.process_id)

    dialog = app.window()
    dialog['StartButton'].click()


def main():
    if not check_run_chaos():
        run_chaos()

    run_starcraft_from_chaos()


if __name__ == '__main__':
    main()
