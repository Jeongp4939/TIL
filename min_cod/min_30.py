"""
# 인접행렬 그래프 DFS

arr = [[0,0,1,1,0,1],
       [0,0,0,1,1,1],
       [0,0,0,0,1,1],
       [0,0,0,0,0,0],
       [1,0,0,0,0,1],
       [0,0,0,0,0,0]]
visited= [0]*6

def dfs(node):
    if not arr[node]:
        return
    print(node,end=' ')
    visited[node] = 1
    for i in range(6):
        if arr[node][i] and not visited[i]:
            dfs(i)

n = int(input())
dfs(n)
"""
"""
# 가중치 인접행렬 DFS

arr = [[0,0,1,0,2,0],
       [5,0,3,0,0,0],
       [0,0,0,0,0,7],
       [2,0,0,0,8,0],
       [0,0,9,0,0,0],
       [4,0,0,7,0,0]]
visited=[0]*6
def dfs(node,level=0,sum=0):
    visited[node] = 1
    print(node, sum)
    if level==6:
        return
    for i in range(6):
        if arr[node][i] and not visited[i]:
            dfs(i,level+1,sum+arr[node][i])
            sum+=arr[node][i]               # 다음 노드에서 진행 못했을 시에 이미 더한 값 보존

n = int(input())
dfs(n)
"""
"""
# 트리 인접 행렬 BFS

arr = [[0,1,0,0,1,0],
       [0,0,1,0,0,1],
       [0,0,0,1,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0],
       [0,0,0,0,0,0]]

visited = [0]*6
queue=[]
def bfs(node):
    print(node, end=' ')

    for i in range(6):
        if arr[node][i] and not visited[i]:
            queue.append(i)
            visited[i]=1
    for i in queue:
        bfs(queue.pop(0))
n = int(input())
bfs(n)
"""
"""
# 그래프 BFS

arr =[[0,0,0,0,1,0],
      [1,0,1,0,0,1],
      [1,0,0,1,0,0],
      [1,1,0,0,0,0],
      [0,1,0,1,0,1],
      [0,0,1,1,0,0]]
queue=[]
visited=[0]*6

def bfs(node):
    visited[node]=1
    print(node)
    for i in range(6):
        if arr[node][i] and not visited[i]:
            queue.append(i)
            visited[i] = 1
    for i in queue:
        bfs(queue.pop(0))

n = int(input())
bfs(n)
"""
"""
# 원형 시계 돌리기

def roll_clock(arr,n):
    if n==0:
        return
    arr[2],arr[0],arr[3],arr[1]=arr[0],arr[1],arr[2],arr[3]
    roll_clock(arr,n-1)

arr = [12,9,3,6]
n = int(input())
n= (n%360)//90

roll_clock(arr,n)
print(*arr)
"""
"""
# 승부차기

def abc(n,s=''):
    if n==0:
        print(s)
        return
    for i in 'ox':
        abc(n-1,s+i)
n=int(input())
abc(n)
"""
"""
# n번째로 큰 숫자

arr = [1,5,4,2,-5,-7]
arr.sort(reverse=True)
n = int(input())
print(arr[n-1])
"""

"""
# 2진수로 된 가장 큰 수를 찾아라

s=[]
rlt=[]
for _ in range(3):
    s.append(input())

Max = 0
idx = 0

max_s=0

for i in s:
    len=0
    point=0
    for j in i:             # 문자열 길이
        len+=1
    for j in range(len):    # 첫 0의 인덱스
        if i[j]=='0':
            point = j
            break
    if len >= Max and point>idx:
        Max = len
        idx = point
        max_s = i
print(max_s)
"""
"""
# 후보 선출하기

s = input()
n = int(input())

def abc(n,s,rlt=''):
    if n==0:
        print(rlt)
        return
    for i in s:
        abc(n-1,s,rlt+i)

abc(n,s)
"""
"""
# 자전거열쇠 비밀번호 맞추기

n = int(input())
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for _ in range(n):
    s = input()
    rlt = 1
    for c in range(len(s)):
        if s[c]=='A':
            continue
        else:
            rlt += 26**(len(s)-c-1)*(alpha.index(s[c]))
    print(rlt)
"""
"""
# 다섯형제 10-20
# 중복 제거해야함

cnt = 0
path=[]
def abc(level=0,idx=0,sum=0):
    global cnt
    if level==5 or sum>20:
        return
    if 10<=sum<=20:
        cnt+=1
    for i in range(5):
        if idx<=i and used[i]!=1:
            idx=i
            path.append(lst[i])
            used[i]=1
            abc(level+1,idx,sum+lst[i])
            path.pop()
            used[i]=0

lst = list(map(int,input().split()))
used = [0]*5
abc()
print(cnt)
"""
"""
# 다시 풀어보는 출동 순서
# 5번째 출동
# 이미 출동한 경우 무시하고 카운트
lst = ['B','I','A','H']
visited=[0]*4
n = int(input())
rlt = []

for i in range(4):
    for j in range(n):
        lst.append(lst.pop(0))
    rlt.append(lst.pop())
print(*rlt)
"""
