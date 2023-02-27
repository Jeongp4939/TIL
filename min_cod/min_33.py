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
"""
# 춘추전국시대

def find(a):
    if arr[ord(a)][0]==0:
        return a
    ret = find(arr[ord(a)][0])
    arr[ord(a)][0]=ret
    return ret

def alliance(a,b): # union
    fa, fb = find(a),find(b)
    arr[ord(fb)][0] = fa
    arr[ord(fa)][1] += arr[ord(fb)][1]
    for i in range(200):
        if arr[i][0]==arr:
            arr[i][1]=arr[ord(fa)][1]

def war(a,b):   # find parent
    global country
    fa, fb = find(a), find(b)
    if arr[ord(fa)][1] > arr[ord(fb)][1]:
        for i in range(200):
            if arr[i][0]==fb:
                arr[i][1]=0
                country-=1

country = int(input())
lst = list(map(int,input().split()))
arr = [[0] for _ in range(200)]

for i in range(country):
    arr[ord('A')+i].append(lst[i])

case = int(input())
# for c in range(case):
#     cmd = input().split()
#     if cmd[0] == 'alliance':
#         alliance(cmd[1],cmd[2])
#         for i in range(country):
#             print(arr[i + 65])
#     elif cmd[0] == 'war':
#         war(cmd[1],cmd[2])

print(5)
"""
"""
n = int(input())
perCnt = {}
nationCnt = {}
isDie = {}
sets = {}

perCnt_list = list(map(int, input().split()))

for i in range(n):
    ch = chr(ord('A') + i)
    nationCnt[ch] = 1
    perCnt[ch] = perCnt_list[i]
    sets[ch] = ch
    isDie[ch] = 0

def find(ch):
    if ch != sets[ch]:
        sets[ch] = find(sets[ch])
    return sets[ch]

def union(a, b):
    if isDie[a] or isDie[b]:
        return
    a, b = find(a), find(b)
    if a == b:
        return
    if perCnt[a] > perCnt[b]:
        a, b = b, a
    perCnt[b] = 0
    isDie[b] = 1
    nationCnt[a] += nationCnt[b]
    sets[b] = a

def war(a, b):
    if isDie[a] or isDie[b]:
        return
    a, b = find(a), find(b)
    if a == b:
        return
    if perCnt[a] > perCnt[b]:
        perCnt[b] = 0
        isDie[b] = 1
        nationCnt[a] += nationCnt[b]
        sets[b] = a
    else:
        perCnt[a] = 0
        isDie[a] = 1
        nationCnt[b] += nationCnt[a]
        sets[a] = b

t = int(input())
for _ in range(t):
    cmd, a, b = input().split()
    if cmd == "alliance":
        union(a, b)
    else:
        war(a, b)

alive = len([k for k, v in isDie.items() if not v])
print(alive+1)
"""

