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

pw = [3,7,4,9]

ipt = list(map(int,input().split()))
cnt = 0
for i in range(len(ipt)):
    if ipt[i] == pw[i]:
       cnt+=1 
    else:
        print('fail')
        break
    if cnt==4:
        print('pass')





