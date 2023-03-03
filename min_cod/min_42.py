"""
# 김밥 속재료

s=input()

def abc(level=3,idx=0,ss=''):
    if level==0:
        print(ss)
        return
    for i in range(len(s)):
        if i>=idx:
            abc(level-1,i,ss+s[i])

abc()
"""
"""
# best Number 선정하기

def dfs(level=0):
    global Max, Min
    if level==5:
        result = calc[0]*calc[1]-calc[2]*calc[3]+calc[4]
        Max=max(Max,result)
        Min=min(Min,result)
        return
    for i in range(5):
        if not used[i]:
            used[i]=1
            calc[level]=numbers[i]
            dfs(level+1)
            used[i]=0

calc=[0]*5
used=[0]*5
numbers= list(map(int,input().split()))

Min = 28e8
Max = -28e8
dfs()
print(Max)
print(Min)
"""
"""
# 가수 BTS와 SES

words=['BTS','SBS','BS','CBS','SES']
Min=28e8
def dfs(level,target,s='',cnt=0):
    global Min
    if level==10 or len(s)>len(target):
        return
    if s==target:
        Min=min(cnt,Min)
        return
    for i in words:
        dfs(level+1,target,s+i,cnt+1)


target = input()
dfs(0,target)
print(Min)
"""
"""
# 최소 동전 교환기

coins=[10,40,60]
Min = 28e8
def dfs(charge,Sum=0,cnt=0):
    global Min
    if charge<Sum:
        return
    if charge==Sum:
        Min = min(Min,cnt)
        return
    for i in coins:
        dfs(charge,Sum+i,cnt+1)

charge=int(input())
dfs(charge)
print(Min)
"""
"""
# 10을 만들자

cnt = 0

def dfs(level,Sum=0):
    global cnt
    if Sum>10:
        return
    if level==0 and Sum==10:
        cnt+=1
        return
    for i in range(1,11):
        dfs(level-1,Sum+i)
n = int(input())
dfs(n)
print(cnt)
"""
"""
# 다빈치 민코드

n,m = map(int,input().split())
lst = list(map(int,input().split()))
num_lst=[0]*m
min_lst=[]
Min = 28e8

def dfs(level,idx=0,mul=1):
    global Min,min_lst
    if level==0:
        if Min > mul:
            Min=mul
            min_lst=num_lst[:]
        return
    for i in range(idx,n):
        num_lst[m-level]=lst[i]
        dfs(level-1,i+1,mul*lst[i])

dfs(m)
min_lst.sort()
print(*min_lst)
"""
"""
# 구매팀 결재

def dfs(lvl,Sum):
    global Max
    if lvl==0:
        if Sum%10==0:
            Max=max(Max,Sum)
        return
    for i in range(7):
        if used[i]:
            dfs(lvl-1,Sum-price[i])

oj = input()
n = int(input())
storage=['a','b','c','d','e','f','g']
price = [15,20,44,22,55,16,45]
used = [0]*7
Sum=0
Max=0
for i in oj:
    id = storage.index(i)
    Sum+=price[id]
    used[id]=1
dfs(n,Sum)
print(Max)
"""
"""
# 레드 마운틴

n=int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
flag= 0

dy,dx=[-1,1,0,0],[0,0,-1,1]
def dfs(y=0,x=0):
    global flag
    if y==n-1 and x==n-1:
        flag=1
        return
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<n and 0<=nx<n:
            if not visited[ny][nx] and not arr[ny][nx]:
                visited[ny][nx]=1
                dfs(ny,nx)
dfs()
if flag:
    print('가능')
else:
    print('불가능')
"""
"""
# 가로 큐브 돌리기

def dfs(level=0):
    global Max
    if level==n:
        mul=1
        for i in ss:
            mul*=i
        Max=max(mul,Max)
        return
    for i in range(n):
        for j in range(n):
            ss[j]+=arr[level][(i + j) % n]
        dfs(level+1)
        for j in range(n):
            ss[j]-=arr[level][(i + j) % n]


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
ss = [0]*n
Max=0

dfs()
print(f'{Max}점')
"""

