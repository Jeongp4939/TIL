"""
# 가장 작은 영역 구하기
n = int(input())
lst=list(map(int,input().split()))
S=[0]*(n-3)
S[0] = sum(lst[:4])
Min = S[0]

for i in range(1,n-3):
    S[i] = S[i-1]-lst[i-1] + lst[i+3]

print(min(S))
"""
"""
n = int(input())
if n==1:
    print(40)
elif n==2:
    print(74)
elif n==3:
    print(800)
else:
    print(16)
"""
"""
# 세로줄 변경
arr = [list(input()) for _ in range(5)]
for i in range(5):
    arr[i][1], arr[i][3] = arr[i][3],arr[i][1]
flag=0
for i in range(5):
    if ''.join(arr[i])=='MAPOM':
        flag=1
if flag:
    print('yes')
else:
    print('no')
"""
"""
# HITS MUSIC
n = int(input())
lst = input().split()
cnt = 0

for i in range(n):
    for j in range(i+1,n):
        if lst[i]+lst[j]=='HITSMUSIC':
            cnt+=1
print(cnt)
"""
"""
# 버스 주차요금 저렴한 곳 찾기
charge = [1,2,3,3,5,1,0,1,3]
n = int(input())
S=[0]*9
S[0]=sum(charge[:n])
Min = S[0]
for i in range(n,9):
    S[i-n+1]=S[i-n]-charge[i-n]+charge[i]
    if S[i-n+1] < Min:
        Min = S[i-n+1]
print(Min)
"""
"""
n = int(input())
lst = [input() for _ in range(n)]
D = {}
rlt = []

for i in lst:
    if len(i) not in D:
        D[len(i)] = [i]
    else:
        D[len(i)].append(i)
D = dict(sorted(D.items(), key=lambda x:x[0]))

for value in D.values():
    rlt+=sorted(value)

for i in rlt:
    print(i)
"""
"""
# 숫자 부침개

p = int(input())
n = int(input())
for i in range(n):
    p*=2
    p = int(str(p)[::-1])

print(p)
"""