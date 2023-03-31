"""
# N-Castle
def dfs(depth,x):
    global cnt
    if depth==N:
        cnt+=1
        return
    for i in range(N):
        if i not in arr:
            arr.append(i)
            dfs(depth+1,i)
            arr.pop()

N = int(input())
cnt = 0
arr=[]
dfs(0,0)
print(cnt)
"""
# N_QUEEN

n=int(input())
dat=[0]*13
rup=[0]*25
rdown=[0]*25
cnt=0

def abc(level):
    global cnt;
    if level==n:
        cnt+=1
        return
    for i in range(n):
        if dat[i]==1: continue
        if rup[level+i]==1: continue
        if rdown[(level-i)+n-1]==1: continue
        rup[level + i] = 1
        rdown[(level - i) + n - 1]=1
        dat[i]=1
        abc(level+1)
        dat[i]=0
        rup[level+i]=0
        rdown[(level - i) + n - 1]=0

abc(0)
print(cnt)
