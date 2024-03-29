# BWAPI_toy
----------------------
## BWAPI 파일들을 이용해 봇을 가지고 노는 토이토이프로젝트입니다.
### 지속적인 버그 수정과 업데이트가 있습니다.
#### Language : Python 3.9.5

----------------------------
## History

### 1.0.12 (2023-09-04)
PSL Season 6 결과가 업데이트 되었습니다.   
이제 RPA_download_bot을 사용해 Bot 파일을 다운로드 할 시 봇 이름 뒤에 업데이트 날짜가 붙어 다운로드 됩니다.   
SSCAIT의 업데이트 로그에 맞춰 반영됩니다.

### 1.0.11 (2023-05-07)
RPA 시스템이 개선되었습니다.   
Chaoslauncher의 실행 파일이 어디 있는지 검색한 후 경로를 저장합니다.   
C 드라이브에 존재하는 ChaosLauncher라면 찾아서 자동으로 실행해 줍니다.   
이제 RPAbwapi로 봇 검색 시 대소문자를 구분하지 않습니다.

### 1.0.10 (2023-05-06)
mmr System Updated. PSL Under League System updated.   
PSL에서 Under League 시스템이 업데이트 되었습니다.   
예선전 하위권 봇들을 가리는 시스템으로 본선에 한 번도 진출하지 못했던 봇은    
전부 Under League 에 들어가게 됩니다.   
바뀐 방식은 본선 진출 경력이 있는 봇을 우선적으로 예선전에 채웁니다.   
남은 자리를 Under League에서 랜덤으로 추출하여 Under League를 예선전과 같은 방식으로 진행합니다. 

mmr 시스템이 업데이트 되었습니다.   
우선 1 vs 1 매치를 생성할 경우 자동적으로 txt파일로 로그를 남깁니다.   
mmr 리그에 다양한 봇들이 추가되었습니다.   
mmr 시스템에 봇 추가 시 이미 있는 봇을 추가하지 못하도록 수정했습니다.

### 1.0.9b (2023-01-28)
RPArunbot을 통해 자동으로 열 수 있는 exe, jar 봇들이 추가되었습니다.
RPArunbot 코드를 약간 개선했습니다.

### 1.0.9 (2023-01-16)
이제 RPA_download_bot에서 봇 파일을 자동으로 업데이트 할 수 있습니다.   
RPA_download_dll에서 해당 봇에 맞는 bwapi.dll파일을 받을 수 있습니다.   
이외에도 봇 정보를 확인하는 단순한 기능들 역시 추가될 예정입니다.

### 1.0.8 (2022-10-06)
PSL Season 5 결과가 업데이트 되었습니다.   
이제 PSL에서 Round Maker 사용 시 16강, 8강, 4강 대진표를 만들 수 있습니다.   
따라서, psl_16_round_maker에서 psl_round_maker로 이름을 변경하였습니다.   

### 1.0.7 (2022-09-02)
이제 RPAbwapi로 봇을 실행 시 자동으로 스타크래프트를 실행합니다.   
또한 해당 봇에 맞는 실행 파일도 같이 실행합니다.   
실행 파일을 안정적으로 실행할 수 있는 배치파일이 추가되었습니다.   
(현재 PurpleWave 봇은 자동 실행할 경우 게임 플레이가 진행되지 않는 버그가 있습니다.)

### 1.0.6 (2022-09-01)
이제 runproleague.py에서 프로리그를 실행할 시 팀을 순서대로 넣을 수 있습니다.   
Team 1과 Team 2의 멤버를 순서대로 넣어 원하는 프로리그 멤버 구성으로 실행할 수 있습니다.   
프로리그 시작 전 팀 순서를 섞을 수 있습니다. (선택지로 제공합니다.)   
RPAbwapi.py의 기능이 개선되었습니다.   
이제 봇 검색 시 여러 봇이 탐색되었을 경우 선택지를 제공합니다.   
(ex. Star 검색 시 BetaStar와 Stardust가 검색되는데 이것을 선택할 권한을 줍니다.)   
RPA_system 파일에 여러 기능을 제공하기 위한 파일들이 추가되었습니다.
아직은 기능을 하고 있지 않으며, 자세한 내용은 각 파일과 앞으로 업데이트할 내용에서 확인할 수 있습니다.   

### 1.0.5 (2022-08-30)
gitignore 파일 업데이트.   
전체적인 파일 구조를 개선했습니다.   
이제 각 기능별로 폴더를 나누어 두었습니다.   

### 1.0.4 (2022-08-23)
mmr.txt를 사용하는 파일들의 시스템을 개선했습니다.   
이제 플레이어의 이름에 공백문이 들어가도 오류가 생기지 않습니다. (공백문이 들어가는 플레이어를 입력할 수 있습니다.)   
추가적으로 공백문을 제거했던 봇들의 이름을 원래대로 되돌렸습니다. (ex. HaoPan -> Hao Pan)   
실제 사용에는 변함이 없습니다.   

### 1.0.3 (2022-08-17)
이제 psl.py 파일에서 PSL과 관련된 기능들을 모두 사용할 수 있습니다.   
명령어를 통해 예선 대진표를 짜거나 대진표 폴더 생성, PSL 맵 추천기, 16강 대진표 만들기 기능을 사용할 수 있습니다.   
psl_map_adviser.py에서 결승전 맵이 5개만 출력되는 버그를 수정했습니다. (7개로 수정)   
psl_16_round_maker.py에서 16강 대진표를 만드는 기능을 제공합니다.   

### 1.0.2a (2022-08-10)
psl_adding_directory.py의 pushing 기능 사용 시 10번째 대진표에 '10 - ' 이 아닌 '010 - '으로 출력되던 버그를 수정했습니다.   
이제 대진표를 직접 작성해서 폴더를 만들 수 있습니다.

### 1.0.2 (2022-08-10)
psl.py에서 이제 대진표를 만들면 draws 폴더에 대진표에 맞는 폴더를 생성해 줍니다.   
psl_adding_directory.py 파일을 통해 해당 기능을 지원합니다.   
psl_map_adviser.py를 통해 16강부터 결승까지의 맵을 추천해줍니다.   

### 1.0.1 (2022-08-04)
runproleague.py가 이제 4:4 뿐만 아니라 3:3, 5:5 등 다양한 숫자의 프로리그를 지원합니다.   
proleaguemaker.py와 randompop.py를 수정하여 runproleague.py에 해당 기능을 제공합니다.   

### 1.0.0 (2022-07-20)
각 파일 추가.
mmr 폴더 생성. view_mmr_order.py 실행 시 내보내는 파일이 저장됨.

---------------------------

## 앞으로 수정할 내용
 
### RPA 시스템 기능 추가
PurpleWave 봇을 자동으로 실행시킬 수 없는 버그를 수정할 예정입니다.   
ChaosLauncher 폴더 등 ChaosLauncher이 포함된 다른 프로세스가 실행 중일 시   
RPA System쪽 기능이 동작하지 않는 버그를 수정할 예정입니다.   
GUI 프로그램화 시킬 때, ChaosLauncher 실행 폴더나 봇 폴더를 직접 지정할 수 있도록 할 예정입니다.
 
### GUI 구현 및 실행 파일화
 아직 크게 정해진 것은 없고 어차피 윈도우 환경에서만 돌아가기 때문에 간단한 GUI 라이브러리를 사용하여 기능들을 편하게 사용하도록 작업을 고민중.   
 최종적으로는 pyinstaller를 사용하여 exe 실행파일로 만드는 것이 목표.
 
### 이외에도 추가하거나 보완할 기능이 생긴다면 업데이트 예정. 
 버전업은 항상 기능적인 부분에서 추가되거나 수정되었을 때 버전을 올린다.   
 간단한 버그나 기능 추가 없는 경우 a, b, c 등의 네이밍으로 옆그레이드.


-----------------------------
### mmr_system

+ calculate_mmr.py
  - 봇들의 mmr을 비교하여 대전 시 적용될 mmr 점수를 계산하여 출력해줍니다.
  - 두 봇의 이름을 검색하여 현재 기준 mmr을 자동으로 불러와 계산하거나
  - mmr 점수를 직접 입력하여 계산받을 수도 있습니다.
  - 현재 mmr 수치는 'mmr.txt' 파일을 참조합니다.
  - 'update_mmr.py' 파일에서 해당 파일을 불러와 mmr을 변경합니다.


+ load_bot_vs_bot.py
  - 'mmr.txt' 파일을 참조하여 봇들을 불러와 랜덤으로 매칭합니다.
  - 매칭된 두 봇의 이름과 mmr을 출력해주며 대전 맵도 랜덤으로 지정하여 출력합니다.
  - 매칭 결과는 '1 vs 1 Match.txt' 파일에 기록합니다.


+ mmr.py
  - 봇 이름을 입력하여 'mmr.txt' 파일에 추가하는 파일입니다.
  - 최초 추가된 봇의 mmr은 2000입니다.
  - 봇 이름에 공백문이 포함되어 있는 경우 충돌하던 버그를 수정하였습니다.
  - 추가적으로 그간 충돌을 피하기 위해 공백문을 제거한 봇 이름들을 원래대로 되돌렸습니다.
  - 이미 존재하는 봇을 추가하지 않습니다.


+ update_mmr.py
  - 'mmr.txt' 파일을 기반으로 봇들의 mmr을 수정하는 파일입니다.
  - 봇의 이름을 검색하여 직접 수정하는 기능도 지원하고, 두 봇의 매치업 결과에 따라 자동으로 mmr 가중치를 계산하여 수정하는 기능도 지원합니다.
  - 봇 이름 검색 시 대소문자를 구별하여 정확하게 입력해야 합니다.


+ view_mmr_order.py
  - 'mmr.txt' 파일을 참조하여 mmr 순으로 출력합니다.
  - 또한 해당 내용을 mmr 폴더에 '(생성 날짜)_MMR Rank.txt' 파일로 내보냅니다.


### proleague_system
+ proleaguemaker.py
  - 봇 이름을 입력하여 Team1과 Team2로 나누어주는 파일입니다.
  - 프로리그 팀을 나누기 위한 함수를 'runproleague.py' 파일에 제공합니다.
  - 멤버 입력 전에 팀을 랜덤으로 섞을 것인지 순서대로 입력할 지 선택할 수 있습니다.


+ randompop.py
  - 봇 이름을 입력하여 그 중 랜덤으로 한 명을 뽑아주는 파일입니다.
  - 'runproleague.py' 파일에 랜덤 픽 함수를 제공합니다.


+ runproleague.py
  - 팀 단위 프로리그를 위한 파일입니다.
  - 봇 이름을 입력해 랜덤으로 팀을 배분한 후 1세트 프로리그, 2세트 위너스리그 (승자연전), 3세트 Ace 결정전 방식으로 진행하게 됩니다.
  - 세트 시작 전 팀 내에서 멤버 순서를 랜덤으로 섞을 것인지 정할 수 있습니다.
  - 최소 2:2 부터 5:5 이상의 팀 단위 플레이를 지원합니다. (단, 홀수 멤버 프로리그는 지원하지 않습니다.)
  - 'proleaguemaker.py' 파일과 'randompop.py' 파일을 임포트하여 해당 파일의 함수를 사용합니다.


### psl_system
+ psl.py
  - PSL과 관련된 기능들을 실행하기 위한 통합 파일입니다.
  - 현재 지원하는 기능은 각각 다음과 같습니다. (명령어 기준)
  - 1 : 봇 개인리그인 psl의 예선 전체 매치업을 작성합니다. (최대 64명)
  - 'submit_bots.txt' 파일에 있는 봇의 이름들을 가져와 랜덤으로 매치시킵니다.
  - 예선은 4인 1조로 되어있으므로 플레이어가 모자라다면 부족한 만큼 공백 문자열을 추가합니다.
  - 참가자 수와 공백 문자열 수를 출력해주며 두 명씩 매치업을 출력합니다.
  - 또한 대진표에 맞게 draws 폴더의 하위 디렉토리에 폴더를 생성합니다.
  - 기존에 사용하고 있는 엑셀 템플릿에 맞게 출력해주는 기능도 지원할 예정입니다.
  - 2 : 대진표를 랜덤으로 출력합니다.
  - psl_16_round_maker.py 파일을 임포트하여 해당 기능을 사용합니다.
  - 16강, 8강, 4강 대진표를 지원합니다.
  - 3 : 대진표에 맞는 폴더를 직접 생성합니다.
  - psl_adding_directory.py 파일을 임포트하여 해당 기능을 사용합니다.
  - 4 : PSL에서 사용할 맵들을 16강부터 결승까지 랜덤하게 출력합니다.
  - psl_map_adviser.py 파일을 임포트하여 해당 기능을 사용합니다.
  - 5 : PSL에 현재 프로게이머 타이틀을 획득한 선수를 출력합니다.
  - psl_check_pro_title.py 파일을 임포트하여 해당 기능을 사용합니다.
  - 6 : Under League를 진행할 수 있도록 봇을 추출해줍니다.
  - 예선전에 필요한 숫자만큼 계산해둬야 합니다.


+ psl_round_maker.py
  - PSL에서 대진표를 랜덤으로 조합해주는 파일입니다.
  - 16강은 Seed 플레이어 4명을 제외한 12명의 플레이어를 입력하여 랜덤으로 Group A부터 D까지 출력합니다.
  - 8강과 4강을 지원하기 시작했습니다.
  - psl.py 파일에 해당 기능을 제공합니다.


+ psl_adding_directory.py
  - psl.py 파일에 대진표에 맞는 폴더 생성 기능을 제공하는 파일입니다.
  - 대진표를 직접 작성하여 폴더를 생성하는 기능을 제공합니다. (make_draws 메소드)
  - 이외에도 psl에 지원할 수 있는 기능들이 이곳에 추가된다면 파일명이 변경될 수 있습니다.


+ psl_check_pro_title.py
  - 현재 PSL에 프로게이머 타이틀을 획득 중인 선수와 프로 타이틀을 빼앗긴 선수들을 출력합니다.
  - 3시즌제를 도입하여 최근 3시즌 내에 본선에 진출하지 못할 시 프로 타이틀을 박탈당합니다.


+ psl_map_adviser.py
  - psl에 사용될 16강부터 결승까지의 맵을 추첨하는 파일입니다.
  - 아직은 단순 콘솔 프린트 기능만 지원합니다.


+ psl_under_league.py
  - psl에 사용될 Under League 출전 봇들을 랜덤으로 추출하기 위한 파일입니다.
  - 예선전에 출전 가능한 숫자를 미리 파악해둬야 합니다.



### RPA_system
+ RPAbwapi.py
  - 봇 이름을 입력하여 자동으로 스타크래프트 폴더에 복사해주는 파일입니다.
  - 사용 편의성을 위해 봇 이름의 전체 이름을 모두 입력할 필요는 없습니다. (ex. BananaBrain 탐색 시 'Bananab' 만 입력 가능)
  - 여러 봇이 검색될 경우 원하는 봇을 선택할 수 있습니다.
  - 대소문자를 구분하지 않고 검색합니다. 숫자나 공백은 여전히 구분합니다.
  - 더 큰 편의성을 위해 버전업이 있을 예정입니다.


+ RPA_download_bot.py
  - SSCAIT 사이트의 api를 이용하여, 최신 버전의 봇 바이너리 파일들을 자동으로 다운로드 하는 파일입니다.   
  - 업데이트 로그를 남겨, 마지막 실행 이후 최신 버전이 추가되었을 경우에만 다운로드합니다.   


+ RPA_download_dll.py
  - 봇의 이름을 입력하여 그에 맞는 bwapi 버전의 dll 파일을 다운로드합니다.   
  - 필요하다면, sscait에 접속하여 api를 호출하는 대신, 직접 봇 버전을 저장하여 사용하게 될 수 있습니다.   


+ RPArunchaos.py
  - chaoslauncher를 자동으로 실행시켜 줍니다.
  - RPAbwapi를 통해 봇 입력 시 자동으로 chaoslauncher도 실행시킬 수 있도록 기능을 제공합니다.
  - 해당 기능을 위해 IDE의 관리자 권한이 필요합니다.
  - 처음 실행 시 ChaosLauncher 폴더가 존재하는 지 여부를 검사한 후 경로를 저장합니다.   
  - RPA 시스템에 오류 발생 시 ChaosLauncher 폴더 등 다른 프로세스가 실행되었는지 확인바랍니다.


+ RPArunbot.py
  - 특정 파일을 실행하여 작동시키는 exe 기반 봇이나 java 기반 봇들을 자동으로 실행시켜 줍니다.
  - RPAbwapi를 통해 봇 입력 시 자동으로 실행 파일을 작동시키는 기능을 제공합니다.
  - run_bat_file 폴더에 있는 배치 파일을 통해 작동시킵니다.
  - 현재 PurpleWave 봇을 자동으로 실행시키면 스타크래프트가 프리징되는 버그가 있습니다.
  - 해당 기능이 수정되기 전까진 PurpleWave는 수동으로 실행시키는 것을 권장합니다.

  
+ get_bot_updated_date.py
  - 봇의 최근 업데이트 날짜를 출력합니다. (SSCAIT의 api 사용)   
  - 필요하면, 모든 sscait 봇을 불러와 업데이트 날짜를 오름차순으로 정렬합니다.   


### not_used
+ make_16_round.py
  - 16강 매치업을 위한 파일입니다.
  - 16개의 봇을 직접 입력하여 (그 이상도 가능하지만 랜덤 16명까지만 뽑고 나머지 제외) 매치업을 출력합니다.
  - 사용 빈도가 적고 다른 파일과 기능도 상당수 겹칠 수 있어 폐기되거나 통합될 수 있습니다.


+ make_team.py
  - 'users.txt' 파일을 참조하여 봇들을 불러와 그룹 별로 나누는 파일입니다.
  - major, middle, underdog으로 그룹을 나누어 출력합니다.
  - 단순히 입력이 들어온 순서대로 나누는 파일이므로 공정성이 적어 폐기되거나 대대적인 수정이 있을 수 있습니다.

  
+ update_users.py
  - 'users.txt' 파일에 플레이어를 입력하는 파일입니다.
  - 추가 기능이 아니므로 실행 시 기존 파일은 덮어씌워집니다.
  - 가급적 실력이 높은 봇을 먼저 입력합니다.

+ path_test.py
  - os로 폴더와 하위 디렉토리 및 파일을 검색하는 예제입니다.
  - ChaosLauncher를 탐색하기 위해 작성되었습니다.
