"""
# cycle 을 찾아라

def find(m):
    if lst[ord(m)]==0:
        return m
    ret = find(lst[ord(m)])
    lst[ord(m)] = ret
    return ret

def union(a,b):
    fa, fb = find(a),find(b)
    lst[ord(b)] = fa

n = int(input())
lst = [0]*101
flag=0
for _ in range(n):
    a,b = input().split()
    if find(a)==find(b):
        flag=1
        break
    union(a,b)
if flag:
    print('발견')
else:
    print('미발견')
"""
"""
# 원시 부족

# 소속 그룹을 찾는 함수
def find(m):
    for i in range(len(lst)):
        if m in lst[i]:
            return i
# 소속 그룹을 합치는 함수
def union(a,b):
    fa,fb = find(a),find(b)
    if fa==fb:
        return
    lst[fa]+=lst[fb]
    lst.pop(fb)

lst = [['A','B','C'],['D','E','F'],['G','H'],['I','J']]
n = int(input())

for _ in range(n):
    a,b = input().split()
    union(a,b)
print(f'{len(lst)}개')
"""
"""
# 인접행렬 cycle 찾기

def find(m):
    if lst[m]==0:
        return m
    ret=find(lst[m])
    return ret

def union(a,b):
    fa,fb = find(a),find(b)
    lst[fb]=fa

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
lst = [0]*n
flag=0
for i in range(n):
    for j in range(i,n):
        if arr[i][j]==1:
            if find(i)==find(j):
                flag=1
                break
            union(i,j)
    if flag:
        break

if flag:
    print('cycle 발견')
else:
    print('미발견')
"""
"""
# Minco 스테이크 하우스

def make_set(n):
    parent=[0]*(n+1)
    for i in range(1,n+1):
        parent[i]=i
    return parent
def find(x):
    if parent[x]!=x:
        return find(parent[x])
    return parent[x]

def union(a,b):
    a,b=find(a),find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,k=map(int,input().split())
parent=make_set(k)
rank={}
temp=[]
for _ in range(n):
    a,b=input().split()
    if a.isdigit() and b.isdigit():
        union(int(a),int(b))
    else:
        if a.isdigit():
            rank[find(int(a))]=b
        else:
            rank[find(int(b))]=a

for i in range(1,k+1):
    print(rank[find(i)],end='')
"""

def alliance():
    pass

def war():
    pass

