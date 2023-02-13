"""
# 삼각관계
lst = {'Amy':'Edger', 'Bob':'Amy', 'Chloe':'Bob','Diane':'Bob', 'Edger':''}
counts = {}
for i in lst.values():
    if i not in counts:
        counts[i]=1
    else:
        counts[i]+=1
max_n=0
max_person = ''
for i in counts.items():
    if i[1]>max_n:
        max_n = i[1]
        max_person=i[0]
print(max_person)
"""
"""
# 보스와 부하들
n = int(input())
nodes = [list(map(int,input().split())) for _ in range(n)]
boss = 0
under = []
for i in range(n):
    if nodes[i][0]==1:
        boss = i

for i in range(n):
    if nodes[0][i] == 1:
        under.append(i)
print(f'boss:{boss}')
print('under:', end='')
print(*under)
"""
"""
# 잃어버린 가족상봉
family = ['A','B','C','D','E','F','G','H']
ar = [[0,1,1,0,0,0,0,1],
      [0,0,0,0,0,0,0,0],
      [0,0,0,1,1,0,1,0],
      [0,0,0,0,0,1,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],]

bro = []
s_idx=family.index(input())
for i in range(8):
    if ar[i][s_idx]==1:
        for j in range(8):
            if ar[i][j] == 1 and j!=s_idx:
                bro.append(j)
if bro:
    for i in bro:
        print(family[i], end=' ')
else:
    print('없음')
"""
"""
# 인접행렬 DFS 시작

def DFS(root=0):
    print(root,end=' ')
    if not nodes[root]:
        return

    visited[root] = 1
    for i in nodes[root]:
        if visited[i]!=1:
            DFS(i)

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

nodes = [[] for _ in range(n)]
visited = [0]*n

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            nodes[i].append(j)

DFS(0)
"""

# 2층에서 경로 출력

path = [0]*3

def DFS(root=0,level=0):
    if not nodes[root] or level==2:
        for i in range(3):
            print(path[i], end=' ')
        print()
        return

    for i in nodes[root]:
        if visited[i]!=1:
            path[level+1]=i
            DFS(i,level+1)

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

nodes = [[] for _ in range(n)]
visited = [0]*n

for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            nodes[i].append(j)

DFS(0)

