import os
import time
import datetime
import fnmatch
import shutil

print(os.getcwd())
os.chdir("C:/Starcraft/bwapi-data/AI/")
print(os.getcwd())

# 파일 경로 만들기
file_path = os.path.join(os.getcwd(), "Monster.exe")
print(file_path)

# 파일의 생성 날짜
create_time = os.path.getctime("Monster.exe")
print(create_time)
print(datetime.datetime.fromtimestamp(create_time).strftime("%Y%m%d %H:%M:%S"))
print(datetime.datetime.fromtimestamp(create_time))

# 파일의 크기 (바이트 단위)
size = os.path.getsize(file_path)
print(size)

# 파일 목록 가져오기
print(os.listdir())
os.chdir("..")
print(os.listdir("AI"))

# 파일 목록 가져오기 (하위 폴더 모두 포함)
os.chdir("..")
result = os.walk("bwapi-data")
print(result)

for roots, dirs, files in result:
    print(roots, dirs, files)

os.chdir("bwapi-data")
result = os.walk(".")
print()

for roots, dirs, files in result:
    print(roots, dirs, files)
print()

# 특정 파일 찾기
name = "Monster.exe"
result = []
for roots, dirs, files in os.walk(os.getcwd()):
    if name in files:
        result.append(os.path.join(roots, name))

print(result)
print()

# 특정 패턴의 파일 찾기
pattern = "*.ini"
result = []

for root, dirs, files in os.walk("."):
    for name in files:
        if fnmatch.fnmatch(name, pattern):
            result.append(os.path.join(root, name))
print(result)
print()


# 주어진 경로가 파일인지 폴더인지 확인
print(os.path.isdir("AI"))
print(os.path.isfile("AI"))

print(os.path.isdir("bwapi.ini"))
print(os.path.isfile("bwapi.ini"))

print()


# 만약 파일/폴더가 존재하지 않는다면? (All False)
print(os.path.isdir("bwapi.ini2"))
print(os.path.isfile("bwapi.ini2"))
print()

# 존재하는지 여부 확인
if os.path.exists("bwapi.ini"):
    print("존재")
else:
    print("존재하지 않음")
print()

# 파일 생성하기 (빈파일)
if os.path.exists("new_file.txt"):
    print('Already Exists!')
else:
    open("new_file.txt", 'a').close()

# 파일 삭제하기
if os.path.exists("new_file_rename.txt"):
    os.remove("new_file_rename.txt")

# 파일명 변경하기
os.rename("new_file.txt", "new_file_rename.txt")


# 폴더만들기
if os.path.exists("new_folder"):
    print("Already Exists!")
else:
    os.mkdir("new_folder")
os.mkdir("C:/rec edit/new_folder")

# 하위 폴더를 가지는 폴더 생성
os.makedirs("C:/rec edit/new_folder/a/b/c")

# 폴더 지우기
os.rmdir("C:/rec edit/new_folder/a/b/c") # 폴더 안이 비었을 때만 삭제 가능

# 폴더명 변경하기
os.rename("C:/rec edit/new_folder/a/b", "C:/rec edit/new_folder/a/c")

# 만약 폴더 안이 비어 있지 않아도 삭제하고 싶다면
shutil.rmtree("C:/rec edit/new_folder")
shutil.rmtree("C:/Starcraft/bwapi-data/new_folder")


# 파일 복사하기
if not os.path.exists("test_folder"):
    os.mkdir("test_folder")
shutil.copy("bwapi.ini", "test_folder")

# 새로운 파일 이름으로 복사하기
shutil.copy("bwapi.ini", "test_folder/copied_bwapi.ini")

# 파일만 확실하게 복사하는 법
shutil.copyfile("bwapi.ini", "test_folder/copied_bwapi_2.ini")

# copy2
shutil.copy2("bwapi.ini", "test_folder/copy2_bwapi_2.ini")

# copy, copyfile : 메타정보 복사 X
# copy2 : 메타정보 복사 O


# 폴더 복사 (새로운 폴더 생성)
shutil.copytree("AI", "test_folder_2")

# 폴더 이동하기
shutil.move("test_folder/copied_bwapi.ini", ".")
