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