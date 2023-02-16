"""
# DFS 시작하기

def DFS(root=0):
    print(root,end=' ')
    if not nodes[root]:
        return

    visited[root]=1
    for i in nodes[root]:
        if visited[i] == 1:
            continue
        DFS(i)


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [0]*(n)
nodes = [[] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            nodes[i].append(j)
# print(nodes)
DFS(0)
"""
"""
# 최소이동 네비게이션

def DFS(root,end,cnt=0):
    if root == end:
        print(cnt)
        return
    elif not nodes[root]:
        print(0)
        return
    visited[root]=1
    for i in nodes[root]:
        if visited[i]!=1:
            DFS(i,end,cnt+1)

arr = [[0,0,1,0,1,1],
       [1,0,0,1,0,0],
       [0,0,0,0,1,0],
       [1,0,0,0,0,0],
       [1,0,0,0,0,0],
       [0,0,0,0,0,0]]
nodes = [[] for _ in range(7)]
visited = [0]*7

for i in range(6):
    for j in range(6):
        if arr[i][j]==1:
            nodes[i+1].append(j+1)

a,b = map(int,input().split())
DFS(a,b)
"""
"""
# 징검다리 돌아오기
lst = [0,3,1,2,1,3,2,1,2,1,0]

def jump(lst,level=0,n=0):
    if level==0:
        print('시작',end=' ')
        print(lst[n], end=' ')
    elif lst[n]!=0:
        print(lst[n],end=' ')

    if n>=len(lst) or lst[n]==0:
        print('도착',end=' ')
        return

    jump(lst,level+1,n+lst[n])

    if level == 0:
        print(lst[n], end=' ')
        print('시작', end=' ')
    else:
        print(lst[n], end=' ')
n = int(input())
jump(lst,0,n)
"""
"""
# 범인의 흔적

evid=[-1,0,0,1,2,4,4]
timeStamp=[8,3,5,6,8,9,10]

def search(n):
    if evid[n]==-1:
        print(f'{n}번index(출발)')
        return
    search(evid[n])
    print(f'{n}번index({timeStamp[n]}시)')
n = int(input())
search(n)
"""
"""
# 모두 같은 숫자일까?
arr = [list(map(int,input().split())) for _ in range(3)]

for i in range(3):
    temp = arr[i][0]
    flag=0
    for j in range(3):
        if temp == arr[i][j]:
            continue
        else:
            flag = 1
            break
    if flag==0:
        print(temp)
    else:
        print('x')
"""
"""
# 두 정렬되어 있는 배열을 하나로
def merge_sort(lst1,lst2):
    max_i = len(lst1)
    max_j = len(lst2)
    i=j=0
    result = []
    while i<max_i and j<max_j:
        if lst1[i] <= lst2[j]:
            result.append(lst1[i])
            i+=1
        else:
            result.append(lst2[j])
            j+=1
    if i==max_i and j!=max_j:
        for jj in range(j,max_j):
            result.append(lst2[jj])
    elif j==max_j and i!=max_i:
        for ii in range(i,max_i):
            result.append(lst1[ii])
    return result

lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))

result = merge_sort(lst1,lst2)
print(*result)
"""
"""
# 블럭을 감싸는 사각프레임 좌표 구하기
arr = [list(map(int,input().split())) for _ in range(4)]
st = []
ed = []
max_cnt = 0
for i in range(4):
    cnt = 0
    for j in range(5):
        if st==[] and arr[i][j] == 1:
            st = [i,j]
        if arr[i][j]==1:
            cnt+=1
            if cnt>max_cnt:
                max_cnt=cnt
                ed = [i,j]
print(f'({st[0]},{st[1]})')
print(f'({ed[0]},{ed[1]})')
"""
"""
# 톱니바퀴
arr = [['3','2','5','3'],
       ['7','6','1','6'],
       ['4','9','2','7']]
def roll(i,n):
    arr[(n)%3][i],arr[(1+n%3)%3][i],arr[(2+n%3)%3][i]= arr[0][i],arr[1][i],arr[2][i]
a,b,c,d = map(int,input().split())
for i,ch in enumerate([a,b,c,d]):
    roll(i,ch)

for line in arr:
    print(''.join(line))
"""
"""
# 지렁이 놓기

a,b = map(int,input().split())

def jirung(a,b):
    lst = ['_'] * 5
    if a>=4 or b==0:
        print(''.join(lst))
        return
    lst[a]=str(b)
    print(''.join(lst))
    jirung(a+1,b-1)
jirung(a,b)
"""
"""
# 움직이는 몬스터

dy,dx=[0,1,0,-1],[1,0,-1,0] # 우 하 좌 상

arr = [list(input()) for _ in range(4)]
monster = {}

for i in range(4):
    for j in range(3):
        if arr[i][j].isalpha():
            monster[arr[i][j]] = [i,j]

monster = dict(sorted(monster.items(),key=lambda x:x[0]))

for i in range(5):
    for j in monster.keys():
        ny = monster[j][0] + dy[i%4]
        nx = monster[j][1] + dx[i%4]
        if 0<=ny<4 and 0<=nx<3:
            if arr[ny][nx].isalpha() or arr[ny][nx]=='#':
                continue
            else:
                arr[ny][nx],arr[monster[j][0]][monster[j][1]] = arr[monster[j][0]][monster[j][1]],arr[ny][nx]
                monster[j][0] += dy[i%4]
                monster[j][1] += dx[i%4]

for line in arr:
    print(''.join(line))
"""
"""
# 같은 단어 찾기
# 두 문장을 입력 받아 가장 긴 공통된 문자열을 출력
s1 = input()
s2 = input()
m1 = len(s1)
m2 = len(s2)
max_len = 0
max_s=''

for i in range(m1):
    for j in range(m2):
        if s1[i] == s2[j]:
            s_len = 0
            s = ''
            for k in range(min(m1-i,m2-j)):
                if s1[i+k]==s2[j+k]:
                    s+=s1[i+k]
                    s_len+=1
                else:
                    break
            if s_len > max_len:
                max_len = s_len
                max_s = s

print(max_s)
"""


