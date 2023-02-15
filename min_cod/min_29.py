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


