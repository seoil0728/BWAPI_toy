import os


path = "C:/"

for file in os.walk(path):
    if 'Chaoslauncher - MultiInstance.exe' in file[2]:
        path = file[0] + '/' + file[2][0]
        print(path.replace('\\', '/'))
