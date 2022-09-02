from pywinauto import application
import pywinauto


def run_chaos():
    chaos = 'C:/Libraries/BWAPI/Chaoslauncher/Chaoslauncher - MultiInstance.exe'
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
