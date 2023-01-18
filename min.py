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




