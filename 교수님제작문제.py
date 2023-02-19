dy = [-1,1,0,0,1,1,-1,-1]
dx = [0,0,-1,1,1,-1,1,-1]

def is_Sink(y,x):
    Max=0
    cnt=0
    for d in range(8):
        ny = y+dy[d]
        nx = x+dx[d]
        if 0<=ny<n and 0<=nx<n:
            if arr[y][x]<arr[ny][nx]:
                cnt+=1
                if arr[ny][nx]-arr[y][x] > Max:
                    Max = arr[ny][nx]-arr[y][x]
    if cnt==8:
        return 1, Max
    return 0 , 0

for tc in range(1,int(input())+1):
    n = int(input())
    rlt = 0
    Max = 0
    arr = [list(map(int,input().split())) for _ in range(n)]
    for i in range(1,n-1):
        for j in range(1,n-1):
            cnt, M = is_Sink(i,j)
            rlt+=cnt
            if M>Max:
                Max=M

    print(f'#{tc} {rlt} {Max}')

