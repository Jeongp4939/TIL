# Git

### 목차

1. [git 초기 설정](#git-초기-설정)

2. [git 기본 명령어](#git-기본-명령어)

    1. [git init](#1-git-init)
    2. [git status](#2-git-status)
    3. [git add](#3-git-add)
    4. [git commit](#4-git-commit)
    5. [git log](#5-git-log)
<br><br><br>

# git 초기 설정

### 최초 한번만 설정

1.  누가 커밋 기록을 남겼는지 확일 할 수 있도록 이름과 메일을 설정

```git
$ git config --global user.name "이름"
$ git config --global user.email "메일 주소"
```

2.  작성자가 올바른지 확인

```git
$ git config --global -l

또는

$ git config --global --list
```

# Git 기본 명령어

## 1. git init

```git
$ git init
Initialized empty Git repository in C:/Users/user/git-practice/.git/
```

- 현재 작업 중인 디렉토리를 Git으로 관리한다는 명령어

- .git 이라는 숨김 폴더를 생성하고, 터미널에는 (master)라고 표기



<font color='red'>주의 사항</font>

1. 이미 Git 저장소인 폴더 내에 또다른 Git 저장소를 만들지 않습니다.
   이미 master가 있다면, git init을 절대 입력하면 안됩니다.

2. 절대로 홈 디렉토리에서 git init을 하지 않습니다. 터미널의 경로가 ~인지 확인합니다.



## 2. git status

```git
$ git status
on branch master

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

- Working Directory와 Staging Area에 있는 파일의 현재 상태를 알려주는 명령어

- 어떤 작업을 시행하기 전에 수시로 status를 확인하면 좋습니다.

- 상태
  
  1.  Untracked : Git이 관리하지 않는 파일(한번도 Staging Area에 올라간 적 없는 파일)
  
  2. Tracked : Git이 관리하는 파일
     
     a. Unmodified : 최신 상태
     
     b. Modified : 수정되었지만 아직 Staging Area에는 반영하지 않은 상태
     
     c. Staged : Staging Area에 올라간 상태

## 3. git add

```git
# 특정 파일
$ git add a.txt

# 특정 폴더
$ git add my_folder/

# 현재 디렉토리에 속한 파일/폴더 전부
$ git add .
```

- Working Directory에 있는 파일을 Stagin Area로 올리는 명령어

- Git이 해당 파일을 추적(관리) 할 수 있도록 만듬

- Untracked, Modified -> Staged로 상태 변경

- 예시
  
  ```git
  $ touch a.txt b.txt
  
  $ git status
  On branch master
  
  No commits yet
  
  Untracked files: # 트래킹 되고 있지 않는 파일 목록
    (use "git add <file>..." to include in what will be committed)
      
      a.txt
      b.txt
  
  nothing added to commit but untracked files present (use "git add" to track)
  ```
  
  ```git
  # a.txt만 Staging Area에 올립니다.
  
  $ git add a.txt
  ```
  
  ```git
  $ git status
  On branch master
  No commits yet
  Changes to be committed: # 커밋 예정인 변경사항(Staging Area)
  (use "git rm --cached <file>..." to unstage)
  new file: a.txt
  Untracked files: # 트래킹 되고 있지 않은 파일
  (use "git add <file>..." to include in what will be committed)
  b.txt
  ```
  
  

## 4. git commit

```git
$ git commit -m "first commit"
[master (root-commit) c02659f] first commit
1 file changed, 0 insertions(+), 0 deletions(-)
create mode 100644 a.txt
```

- Staging Area에 올라온 파일의 변경 사항을 하나의 버전(커밋)으로 저장

- 커밋 메세지는 현재 변경 사항들을 잘 나타낼 수 있도록 <font color='red'>의미</font>있게 작성하는 것을 권장함

- root-commit은 해당 커밋이 최초의 커밋 일 때만 표시



## 5. git log

- commit의 내역(ID, 작성자, 시간, 메세지 등)을 조회 할 수 있는 명령어

- 옵션
  
  - --online : 한 줄로 축약해서 보여줍니다.
  
  - --graph : 브랜치와 머지 내역을 그래프로 보여줍니다.
  
  - --all : 현재 브랜치를 포함한 모든 브랜치의 내역을 보여줍니다.
  
  - --reverse : 커밋 내역의 순서를 반대로 보여줍니다.(최신이 가장 아래)
  
  - -p : 파일의 변경 내용도 같이 보여줍니다.
  
  - -2 : 원하는 갯수 만큼의 내역을 보여줍니다.(2 말고 임의의 숫자 가능)

