""" 
# lst=[['D','A','T','A','W'],['B','B','Q','K']]

# n = int(input())

# if n%2:
#     lst[0].sort()
# else:
#     lst[1].sort()
    
# for i in range(2):
#     for j in range(len(lst[i])):
#         print(lst[i][j],end='')
#     print()

# lst = [['P','O','T','I','O'],['A','B','C','D','E'],['Y','O','U','R','E']]
# lst_choose=[]
# a, b = map(int, input().split())
# for li in lst:
#     for i in range(a,b+1):
#         lst_choose.append(li[i])
# for i in lst_choose:
#     print(i,end='')

# print('''1234
#  567
#   89
#    0''')

# print(f'158% 입니다')

# q,w,e = 1,2,3
# print(f'''#q={q},{q},{q}
# #w={w},{w},{w}
# #e={e},{e},{e}''')

# a = 10
# print(f'a의 값은 {a}입니다')

# bbq=5
# print(f'bbq의 값은 {bbq}입니다')

# a,b,c = 40,60,10
# g=a+c
# h=b-c
# print(g)
# print(h)

# a,b = 10,3
# print(f'''{a} * {b} = {a*b}
# {a} / {b} = {a//b}''')

# a,b,c,d = 3,2,6,2
# print(f'{(a+b)*(c//d)}')

# a,b,c,d = 3,3,8,3
# print(f'{(a*b)+(c*d)}')

# n = int(input())
# print(f'{n} 입력하셨군요')

# a,b,c = map(int,input().split())
# print(f'''{a}{a}{a}
# {b}{b}{b}
# {c}{c}{c}''')

# a, b = map(int,input().split())
# print(f'두 숫자의 차는 {a-b} 입니다.')

# a, b = map(int,input().split())
# print(f'''{a}+{b}={a+b}
# {a}*{b}={a*b}
# {a}/{b}={a//b}''')

# a, b = map(int,input().split())
# print(f'a가b보다크다') if a>b else print(f'b가a보다같거나크다')

# a = int(input())
# print(f'''{a} 입력함
# a++을 수행하면 {a+1}이 됩니다''')

# n = int(input())
# print(n+1) if n>3 else print(n-1)

# n = int(input())
# print('###\n###\n###') if n>0 else print('$$$\n$$$')

# print(f'WWW."MIN"CODING.CO.KR')

# a,b = map(int,input().split())
# print('같습니다') if a==b else print('다릅니다')

# a,b,c = map(int,input().split())
# print(f'첫번째 숫자는 {a} 입니다.')
# print(f'두번째 숫자는 {b} 입니다.')
# print(f'세번째 숫자는 {c} 입니다.')

# a,b,c,d = map(int,input().split())
# print(f'''a + b = {a+b}
# c + d = {c+d}
# ALL SUM = {a+b+c+d}''')

# a,b,c = map(int,input().split())

# if a==b:
#     if a==c:
#         print('만세')

# b1, b2, b3, b4 = map(int,input().split())
# if b1>=b2:
#     if b1>=b3:
#         if b1>=b4:
#             print('b1이 가장 크다')


# a,b,c,d = map(int,input().split())
# m = (a+b+c+d)//4
# for i in [a,b,c,d]:
#     if i<m: print(f'{i}<{m}')
#     elif i==m: print(f'{i}=={m}')
#     else: print(f'{i}>{m}')

# a,b = map(int,input().split())
# print('멀다') if (a-b if a>b else b-a)>5 else print('가깝다')

# a,b = map(int,input().split())
# if a+b>10:
#     print('합만세')
# if a*b>10:
#     print('곱만세')

# lst = list(map(int,input().split()))
# print(*lst[-4:])

# for _ in range(10):
#     print('#',end='')

# a,b = map(int,input().split())
# if a>b:
#     print(f'큰수는 {a}')
# elif a==b:
#     print('같은숫자')
# else:
#     print(f'큰수는 {b}')

# n = int(input())
# print('만세') if n==5 or n==10 else print('재도전')


# a,b = map(int,input().split())
# if a==7 and b==9:
#     print('인증됨')
# else:
#     print('재시도')

# a,b = map(int,input().split())
# for i in range(a,b+1):
#     print(i)

# for _ in range(25):
#     print('PIZZAHOT')

# for i in range(10,0,-1):
#     print(i)

# n = int(input())
# if (n*2+20)//5 != 100:
#     print("Magic")

# a,b = map(int, input().split())
# for i in range(a,b+1):
#     print(i,end='')

# n = int(input())

# for i in range(n+1):
#     print(i)

# a,b,c = map(int,input().split())

# if a+b+c > 10:
#     print(a*b*c)
# else:
#     print(0)

# for i in range(-5,6):
#     print(i, end=' ')
    
# for i in range(3,9):
#     print(i, end=' ')
    
# n = int(input())
# for i in range(n,n+3):
#     print(str(i)*3)

# pw = input()
# if pw=='1 2 3 4':
#     print('로그인성공')
# else:
#     print('로그인 실패')

# n = int(input())

# for i in range(n+2,n+5):
#     print(i, end=' ')

# a,b,c = map(int,input().split())
# if a==max(a,b,c):
#     print("MAX발견")
# if a==max(a,b,c):
#     print("MAX아님")

# a,b = map(int,input().split())

# if 30<a*b<50:
#     print('적당한 사이즈')
# elif a*b>=50:
#     print('큰 사이즈')
# else:
#     print('작은 사이즈')

# a,x = map(int,input().split())

# for i in range(a-1, a-x-1,-1):
#     print(i, end=' ')

# a,b,c = map(int,input().split())
# for i in range(a,b+1):
#     print(i, end=' ')
# print()
# for i in range(a,c+1):
#     print(i, end=' ')

# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# arr = [[' ' for _ in range(3)] for _ in range(3)]

# a = input()
# alph_ = alphabet[alphabet.find(a):]
# i,j = 2,0
# n=0
# # arr[2][0]
# # arr[1][0] arr[1][1]
# # arr[0][0] arr[0][1] arr[0][2]

# while i >= 0:
#     while j<=2-i:
#         arr[i][j] = alph_[n]
#         n+=1
#         j+=1
#     i-=1
#     j=0
# for i in arr:
#     for j in i:
#         print(j,end='')
#     print()


# result = ''

# for _ in range(3):
#     str_ipt = input()
#     result+=str_ipt[-1]
# print(result)

# arr=[['A','B','K','T'],
#      ['K','F','C','F'],
#      ['B','B','Q','Q'],
#      ['T','P','Z','F']]

# a,b = map(str,input().split())
# cnt = 0
# for arr_line in arr:
#     if a in arr_line:
#         cnt += arr_line.count(a)
#     if b in arr_line:
#         cnt += arr_line.count(b)
# print(cnt)

# s = input()
# n = int(input())

# s = s[:n]+'A'+s[n:]
# print(s)

# A = list(map(int,input().split()))
# B = list(map(int,input().split()))

# result=[0 for _ in range(4)]

# for i in range(4):
#     result[i] = A[i]+B[3-i]

# print(*result)

# s = input()
# n = int(input())

# print(s[:n]+s[n+1:])

# arr = list(map(int,input().split()))

# for i in range(1,len(arr)):
#     arr[i] += arr[i-1]

# print(*arr) 

# flag = False
# for _ in range(3):
#     if 'M' in input():
#         flag = True

# if flag:
#     print('M이 존재합니다')
# else:
#     print('M이 존재하지 않습니다')

# a,b,c = map(int,input().split())

# for i in range(c):
#     print(*range(a,b+1))
        
# arr = [[0 for _ in range(3)] for _ in range(6)]
# cnt = 65
# for i in range(2,-1,-1):
#     for j in range(5,-1,-1):
#         arr[j][i]=chr(cnt)
#         cnt+=1

# row,col = map(int,input().split())

# print(arr[row][col])

# arr = [[0 for _ in range(3)] for _ in range(2)]
# lst = list(map(int,input().split()))

# max_n,min_n=lst.index(max(lst)),lst.index(min(lst))

# print(f'({max_n//3},{max_n%3}),({min_n//3},{min_n%3})')

# arr = [0 for _ in range(6)]
# arr[0],arr[1] = map(int,input().split())
# for i in range(2,6):
#     arr[i] = arr[i-1]*arr[i-2]
# print(arr[-1])

# s = input()

# ch1=input()
# ch2=input()

# while ch1 in s:
#     s=s.replace(ch1,ch2)
# print(s)

# s= input()
# s_lst = sorted(list(s))

# print(s.index(s_lst[-1]))
# print(s.index(s_lst[0]))

# arr=[[i+j*4 for i in range(1,5)] for j in range(7)]

# n_list = list(map(int,input().split()))

# for i in n_list:
#     for j in range(4):
#         arr[i][j]=0
        
# for line in arr:
#     print(*line)

# arr=[['A',7,9,'T','K','Q'],['M','I','N','C','O','D']]
# a_flag=False
# b_flag=False
# a,b = input().split()
# for i in arr:
#     if a in i:
#         a_flag=True
#     if b in i:
#         b_flag=True
# print(f'{a} : 존재') if a_flag else print(f'{a} : 없음')
# print(f'{b} : 존재') if b_flag else print(f'{b} : 없음')


# s=list(input().split())
# for i in range(int(s[0])):
#     for J in range(int(s[1])):
#         print(s[2],end='')
#     print()
# print()
# for i in range(int(s[0])):
#     for J in range(int(s[1])):
#         print(s[2],end='')
#     print()


# arr = ['M','T','K','C']
# c = input()
# print('발견') if c in arr else print('미발견')

# arr = [5,9,4,6,1,5,8,9]

# idx,target = map(int,input().split())
# tg_idx = arr.index(target)
# print(f'{tg_idx-idx}') if tg_idx>=idx else print(f'{len(arr)-idx+tg_idx}')


# arr=[[3,5,9],[4,2,1],[1,1,5]]

# marking = [list(map(int,input().split())) for _ in range(3)]

# result = 0
# for i in range(3):
#     for j in range(3):
#         if marking[i][j]==1:
#             result+=arr[i][j]
# print(result)


# arr=[['A','T','K','B'],['C','Z','F','D'],['H','G','E','I']]

# c,y,x=input().split()
# x,y = int(x),int(y)
# on_x,on_y = 0,0
# for line in arr:
#     if c in line:
#         on_y, on_x = arr.index(line), line.index(c)
# print(arr[on_y+y][on_x+x])

# arr = [[3,5,9],[4,2,1],[5,1,5]]

# a_flag,b_flag,c_flag = False,False,False
# a,b,c=map(int,input().split())

# for line in arr:
#     if a in line:
#         a_flag=True
#     if b in line:
#         b_flag=True
#     if c in line:
#         c_flag=True

# print(f'{a}:존재') if a_flag else print(f'{a}:미발견')
# print(f'{b}:존재') if b_flag else print(f'{b}:미발견')
# print(f'{c}:존재') if c_flag else print(f'{c}:미발견')

# arr1 = [[0,0,0,1],[1,1,0,1],[1,0,0,1],[1,1,1,1]]
# arr2 = [[1,1,1,1],[1,0,1,1],[1,0,0,0],[1,0,0,0]]
# arr = [[0 for i in range(4)]for _ in range(4)]

# for i in range(4):
#     for j in range(4):
#         arr[i][j]=(arr1[i][j] or arr2[i][j])

# for i in range(4):
#     for j in range(4):
#         if arr[i][j] == 0:
#             print(f'({i},{j})')

# mask = [[0,0,1,0,0],[0,0,1,1,1]]
# arr = [[3,5,4,1,1],[3,5,2,5,6]]

# lst=[]

# for i in range(len(mask)):
#     for j in range(len(mask[i])):
#         if mask[i][j]==1: lst.append(arr[i][j])

# n = int(input())

# print(f'{n} 존재') if n in lst else print(f'{n} 없음')

# arr = ['B','T','K','I','G','Z']
# target = list(input().split())
# cnt = 0
# for c in target:
#     if c in arr:
#         cnt+=1
# print(cnt)

# vect = [[3,7,4],[2,2,4],[2,2,5]]
# target = list(map(int,input().split()))
# cnt = [0,0,0]
# for i in range(3):
#     for line in vect:
#         if target[i] in line:
#             cnt[i]+=1
# print(max(cnt))
    
# lst = [3,4,1,1,2,6,8,7,8,9,10]
# def getSum(index,arr=lst):
#     return sum(lst[index:index+5])

# n = int(input())
# print(getSum(n))
    
# def isExist(n):
#     lst = [3,7,4,1,2,6]
#     result='OK' if n in lst else 'NO'
#     return result
    
# arr = []
# for _ in range(2):
#     arr.append(list(map(int,input().split())))
    
# for i in range(2):
#     for j in range(2):
#         arr[i][j] = isExist(arr[i][j])

# for line in arr:
#     print(*line)

# a=input()
# b=input()

# print('동명') if a==b else print('남남')

# def isExist(ipt):
#     lst = [['G','K','T'],['P','A','C']]
#     result = 0
#     for ls in lst:
#         result+=ls.count(ipt[0])+ls.count(ipt[1])
#     return result

# A = list(input().split())
# if isExist(A) == 2:
#     print('대발견')
# elif isExist(A) == 1:
#     print('중발견')
# else:
#     print('미발견')


# vect = [3,5,4,2,6,6,5]
# bit = list(map(int,input().split()))

# for i in range(len(vect)):
#     vect[i]=7 if vect[i] and bit[i] else 0
# for i in vect:
#     print(i,end='')

# pw = [3,7,4,9]

# ipt = list(map(int,input().split()))
# cnt = 0
# for i in range(len(ipt)):
#     if ipt[i] == pw[i]:
#        cnt+=1 
#     else:
#         print('fail')
#         break
#     if cnt==4:
#         print('pass')


# levelTable = [[10,20],[30,60],[100,150],[200,300]]
# level = {'lev0':0,'lev1':0,'lev2':0,'lev3':0}
# fruits = list(map(int,input().split()))

# for fruit in fruits:
#     for i in range(len(levelTable)):
#         if levelTable[i][0]<=fruit<=levelTable[i][1]:
#             level['lev'+str(i)] += 1
# for lev,cnt in level.items():
#     print(f'{lev}:{cnt}')


# 컬러 찾기

# def isExist(n, arr):
#     for line in arr:
#         if n in line:
#             return 'Y'
#     return 'N'

# map_n = [[3,55,42],[-5,-9,-10]]
# pix = []
# for _ in range(2):
#     pix.append(list(map(int,input().split())))
# for pix_line in pix:
#     for p in range(len(pix_line)):
#         pix_line[p] = isExist(pix_line[p],map_n)
# for line in pix:
#     print(*line)




# dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


# def dfs(start):
#     visit = [[0]*16 for _ in range(16)]     # 16x16의 빈 배열 생성(경로 저장용)
#     stack = [start]                         # 시작점 좌표
#     while stack:                            # 스택이 빌 때까지 반복
#         y, x = stack.pop()
#         if visit[y][x] == 0:                # 가보지 않은 경로이면 지나갔으니 체크
#             visit[y][x] = 1
#             for i in range(4):              # 4방향 조사
#                 ny = y + dy[i]
#                 nx = x + dx[i]
#                 if data[ny][nx] == '0':     # 안가본 위치라면 스택에 다음 좌표 삽입
#                     stack.append([ny, nx])
#                 elif data[ny][nx] == '3':   # 도착점에 도착하면 1을 반환하고 끝
#                     return 1
#     return 0                                # 도착점에 도착 못하면 0을 반환


# for t in range(1, 11):  # 10번의 테스트 케이스를 받은
#     input()             # 입력만 받고 안쓰는 인풋
#     data = [input() for i in range(16)]
#     print('#{} {}'.format(t, dfs([1, 1])))


# def bbq():
#     return bbq()


# n = int(input())

# def bunji(n):
#     print(n,end=' ')
#     if n > 0:
#         bunji(n-1)
#     if n!=0:
#         print(n,end=' ')
# bunji(n)

# for i in range(len(arr)):
#     print(arr[i], end=' ')
# for i in range(len(arr)-2,-1,-1):
#     print(arr[i],end=' ')

# def jackson(arr,n=0):
#     print(arr[n],end=' ')
#     if n==len(arr)-1:       # n이 arr의 마지막 인덱스일 경우 종료
#         return
#     elif n<len(arr)-1:      # 다음 인덱스 호출을 위한 검사
#         jackson(arr,n+1)
#     print(arr[n],end = ' ')

# arr = list(map(int, input().split()))
# jackson(arr)

# cnt=0
# def abc(n):
#     global cnt
#     cnt+=1
#     if cnt <= 3:
#         abc(n+2)
#     print(n,end=' ')

# n=int(input())    
# abc(n)
    

# map = [[65000, 35, 42, 70],
#        [70, 35, 65000, 1300],
#        [65000, 30000, 38, 42]]

# dic = {}
# for line in map:
#     for i in line:
#         if i not in dic:
#             dic[i]=1
#         else:
#             dic[i]+=1
# dic = sorted(dic.items(),key=lambda x:x[1],reverse=True)
# print(dic[0][0])

# arr = [list(map(int,input().split())) for _ in range(3)]
# one_to_nine=[1,2,3,4,5,6,7,8,9]

# for line in arr:
#     for i in line:
#         if i in one_to_nine:
#             one_to_nine.remove(i)
# one_to_nine.sort()
# print(*one_to_nine)
    
    
    
# map=[[1, 3, 3, 5, 1],
#     [3, 6, 2, 4, 2],
#     [1, 9, 2, 6, 5]]

# n=int(input())

# dic = {}
# for line in map:
#     for i in line:
#         if i not in dic:
#             dic[i]=1
#         else:
#             dic[i]+=1

# check=[]

# for key,value in dic.items():
#     if value == n:
#         check.append(key)
# check.sort()
# print(*check)
    


# cardlist=input()
# cnt = {}
# for i in cardlist:
#     if i not in cnt:
#         cnt[i]=1

# print(f'{len(cnt.keys())}개')


# S=input()
# cnt = {}
# for i in S:
#     if i not in cnt:
#         cnt[i]=1
#     else:
#         cnt[i]+=1
# cnt = sorted(cnt.items(),key=lambda x:x[1],reverse=True)
# print(f'{cnt[0][0]}')


# town = [['C','D','A'],['B','M','Z'],['Q','P','O']]
# black = input()
# cnt=0

# for line in town:
#     for i in line:
#         if i in black:
#             cnt+=1
            
# print(f'{cnt}명')

# map = [['A', 'B', 'C'],
#     ['A', 'G', 'H'],
#     ['H', 'I', 'J'],
#     ['A', 'B', 'C'],
#     ['K', 'A', 'B']]

# s=''
# for line in map:
#     for i in line:
#         s+=i
# s=''.join(sorted(s))
# print(s)

# train = [3,7,6,4,2,9,1,7]
# train_str=''
# team = ''.join(input().split())
# for i in train:
#     train_str+=str(i)
# idx = train_str.index(team)
# print(f'{idx}번~{idx+len(team)-1}번 칸')



# apt = [[15, 18, 17],
#         [4, 6, 9],
#         [10, 1, 3],
#         [7, 8, 9],
#         [15, 2, 6]]

# people=list(map(int,input().split()))

# for i in range(len(apt)):
#     if apt[i]==people:
#         print(f'{5-i}층')

# arr = [[3,5,4],[1,1,2],[1,3,9]]
# rlt=0
# y,x = map(int,input().split())
# dy=[-1,1,0,0]
# dx=[0,0,1,-1]

# for i in range(4):
#     if 0<=y+dy[i]<3 and 0<=x+dx[i]<3:
#         rlt += arr[y+dy[i]][x+dx[i]]
# print(rlt)

# dy=[-1,-1,1,1]
# dx=[-1,1,-1,1]
# arr = [[3,3,5,3,1],
#        [2,2,4,2,6],
#        [4,9,2,3,4],
#        [1,1,1,1,1],
#        [3,3,5,9,2]]

# def sum_d(y,x):    
#     sum_ = 0
#     for i in range(4):
#         if 0<=y+dy[i]<5 and 0<=x+dx[i]<5:
#             sum_ += arr[y+dy[i]][x+dx[i]]
#     return y,x,sum_


# max_coord_y=max_coord_x=max_sum=0

# for i in range(5):
#     for j in range(5):
#         if max_sum<sum_d(i,j)[2]:
#             max_coord_y,max_coord_x,max_sum = sum_d(i,j)
    
# print(max_coord_y,max_coord_x)

# ground=[['_' for _ in range(5)] for _ in range(4)]
# dy=[1,-1,0,0,1,1,-1,-1]
# dx=[0,0,-1,1,1,-1,1,-1]

# def boom(y,x):    
#     for i in range(8):
#         if 0<=y+dy[i]<4 and 0<=x+dx[i]<5:
#             ground[y+dy[i]][x+dx[i]]='#'

# for i in range(2):
#     y,x = map(int,input().split())
#     boom(y,x)

# for line in ground:
#     print(*line)



# a=list(map(int,input().split()))
# b=list(map(int,input().split()))

# for i in range(3):
#     print(a[i]+b[i])


# arr = [['G','K','G']]
# arr.append(input().split())
# arr = arr[0]+arr[1]

# for i in arr:
#     if arr.count(i)>=3:
#         print('있음')
#         break
# else:
#     print('없음')


# lst=list(input().split())
# for i in lst:
#     if lst.count(i)>=2:
#         print('도플갱어 발견')
#         break
# else:
#     print('미발견')

# S = input()
# max_cnt=0
# max_chr=''
# for i in S:
#     if S.count(i) > max_cnt:
#         max_cnt=S.count(i)
#         max_chr=i
# print(max_chr)


# up = list(map(int,input().split()))
# down = list(map(int,input().split()))
# cnt=0
# for i in range(len(up)):
#     if up[i] & down[i]:
#         cnt+=1
# print(f'{cnt}개')


# s = 'ATKPTCABC'

# a,b = input().split()

# a_idx=s.index(a)
# b_idx=len(s)-list(reversed(s)).index(b)-1

# print(max(a_idx,b_idx)-min(a_idx,b_idx))

# win = [[3,5,1],[4,2,6]]
# people = list(map(int,input().split()))

# for i in people:
#     for winner in win:
#         if i in winner:
#             print(f'{i}번 합격')
#             break
#     else:
#         print(f'{i}번 불합격')


# vect = 'MINCODING'
# input()
# c_lst = list(input().split())

# for c in c_lst:
#     if c in vect:
#         print('O',end='')
#     else:
#         print('X',end='')

# s_lst=[]
# for _ in range(3):
#     s_lst.append(input())
# flag=False

# for s in s_lst:
#     for c in s:
#         if s.count(c)>=2:
#             flag=True
#             break
#     if flag:
#         print('No')
#         break
# else:
#     print('Perfect')


# s = input()
# new_s=''

# for c in s:
#     if c not in new_s:
#         new_s+=c
# print(''.join(sorted(new_s)))

# s=input()
# s_dic={}
# for c in s:
#     if c not in s_dic:
#         s_dic[c]=1
#     else:
#         s_dic[c]+=1

# s_dic=sorted(s_dic.items(), key=lambda x:x[0])

# for s_ in s_dic:
#     print(f'{s_[0]}:{s_[1]}')

# s = input()

# if 'GHOST' in s:
#     print('존재')
# else:
#     print('존재하지 않음')

# bob = [input()for _ in range(2)]
# tom = [input()for _ in range(2)]

# for i in range(2):
#     print(f'bob.burger{i+1}={len(bob[i])}')
# for i in range(2):
#     print(f'tom.burger{i+1}={len(tom[i])}')

# train=[[15, "summer"],
#     [33, "cloe"],
#     [24, "summer"],
#     [28, "niki"],
#     [32, "jenny"],
#     [20, "summer"],
#     [40, "coco"]]

# person = [input() for _ in range(2)]

# for i in range(len(train)):
#     if train[i][1]==person[0] and train[i][0]==int(person[1]):
#         print(i)
        

# vect = [[0]*3 for _ in range(4)]

# ipt = [list(map(int,input().split())) for _ in range(4)]
# for y,x in ipt:
#     vect[y][x]=5
# for line in vect:
#     print(*line)

# image = [list(map(int,input().split())) for _ in range(4)]
# coord = (0,0)
# max_sum=0
# for i in range(3):
#     for j in range(2):
#         if max_sum < image[i][j]+image[i][j+1]+image[i][j+2]+image[i+1][j]+image[i+1][j+1]+image[i+1][j+2]:
#             max_sum = image[i][j]+image[i][j+1]+image[i][j+2]+image[i+1][j]+image[i+1][j+1]+image[i+1][j+2]
#             coord=(i,j)
# print(f'({coord[0]},{coord[1]})')

# def BBQ(lst):
#     return max(lst),min(lst)

# lst = list(map(int,input().split()))
# a,b=BBQ(lst)
# print(f'a={a}')
# print(f'b={b}')

# ground = [list(map(int,input().split())) for _ in range(5)]
# dy,dx=[0,0,1,-1,1,1,-1,-1],[1,-1,0,0,1,-1,1,-1]

# def is_stable(ground):
#     for i in range(5):
#         for j in range(4):
#             if ground[i][j]==1:
#                 for d in range(8):
#                     ny = i+dy[d]
#                     nx = j+dx[d]
#                     if ny<0 or nx<0 or ny>=5 or nx>=4:
#                         continue
#                     if ground[ny][nx]==1:
#                         return '불안정한 상태'
#     return '안정된 상태'

# print(is_stable(ground))
 """

""" 
arr = [[i for i in range(4*j+1,4*j+4+1)] for j in range(4)]
new_arr = [[0]*4 for _ in range(4)]

pw = list(map(int,input().split()))
coord=[]
for p in pw:
    for i in range(4):
        for j in range(4):
            if arr[i][j]==p:
                coord.append((i,j))
for i in range(4):
    new_arr[coord[i][0]][coord[i][1]]=i+1

for line in new_arr:
    print(*line)
                

"""
""" 
# 가로 세로 색칠하기
# 4x4 배열

arr = [[0]*4 for _ in range(4)]

for _ in range(3):
    a,b = map(str,input().split())
    if a == 'G':
        for i in range(4):
            arr[int(b)][i]=1
    elif a == 'S':
        for i in range(4):
            arr[i][int(b)]=1

for line in arr:
    print(*line)

"""
""" 
# 모양 넣기
image = [input()for _ in range(3)]
alpha=[]
for i in range(3):
    for j in range(3):
        if image[i][j] not in alpha:
            alpha.append(image[i][j])
print(''.join(sorted(alpha)))
"""
""" 
# 비밀 위치 찾기
arr=[['A','B','G','K'],['T','T','A','B'],['A','C','C','D']]
pattern = [input() for _ in range(2)]

cnt=0
for i in range(2):
    for j in range(3):
        if arr[i][j]+arr[i][j+1]==pattern[0] and arr[i+1][j]+arr[i+1][j+1]==pattern[1]:
            cnt+=1

if cnt:
    print(f'발견({cnt}개)')
else:
    print('미발견')
"""
""" 
# 마스킹하고 난 뒤

arr = [[3,5,1],[3,8,1],[1,1,5]]
bitarray = [list(map(int,input().split())) for _ in range(2)]


max_sum = 0
y=x=0

for i in range(2):
    for j in range(2):
        sum = 0
        for bi in range(2):
            for bj in range(2):
                if bitarray[bi][bj]:
                    sum+=arr[i+bi][j+bj]
        if sum>max_sum:
            max_sum=sum
            y,x = i,j
print(f'({y},{x})')
"""


# 다섯 글자 역순 출력 재귀함수 이용

def reverse_str(s):
    pass
    


s='asdfg'

print(reverse_str(s))

    



































































