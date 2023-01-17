'''
조건문
반복문
함수
map filter
lambda
'''

# a=int(input())
# if a>5:
#     print('오삼')
# elif a>3:
#     print('불고기')
# elif a>4 or a==-1:
#     print('재시도')
# else:
#     print('오삼불고기')

# 숫자 2개 입력 받은 후
# 둘 중 큰 수를 출력해 주세요

# a , b = map(int, input().split())
# if a>b:
#     print(a)
# elif a<b:
#     print(b)
# else:
#     print('같습니다.')
    
# result=a if a>b else b      # 조건표현식
# print(result)

# for i in range(1,101):
#     print('#'+' '+str(i),end=' ')

# print()

# i=1
# while i<=100:
#     print(f'# {i}',end=' ')
#     i += 1

# 리스트 출력 for문 이용하여 출력하기
# lst=[[1,2,3],[4,5,6]]

# for ls in lst:
#     print(*ls)
    
# for i in range(0,2):
#     for j in range(0,3):
#         print(lst[i][j],end=' ')

# 1차원 리스트
# 빈 리스트 하나 만든 후 lst 의 값들에 제곱을 한 값으로 채워넣기
# 새로 만들어진 리스트를 출력하기
# lst=[[1,2,3],[4,5,6]]
# multi = []

# for i in lst:
#     for j in i:
#         multi.append(j**2)
# print(*multi)

# 제곱근을 이차원 리스트에 담아보기
# (multi를 이차원 리스트로 만들것임)

# lst=[[1,2,3],[4,5,6]]
# multi = []

# for li in lst:
#     temp=[]
#     for i in li:
#         temp.append(i**2)
#     multi.append(temp)

# for li in multi:
#     for i in li:
#         print(i,end=' ')
#     print()

# 딕셔너리

# di ={'kevin':1, 'john':2,'bob':3}

# print(di)
# for i in di:
#     print(i,di[i])
# for i,j in di.items():
#     print(i,j)

# lst = [[1,2,3],[1,2,3],[1,2,3]]
# for i in range(3):
#     for j in range(3):
#         if lst[i][j]==3:
#             break
#         print(lst[i][j],end=' ')
# # 1 2 1 2 1 2 

# lst = [[1,2,3],[1,2,3],[1,2,3]]
# for i in range(3):
#     for j in range(3):
#         if lst[i][j]==2:
#             continue
#         print(lst[i][j],end=' ')
# 해당 수를 제외하고 출력

# 함수 내장, 외장, 사용자
# lst = [1,2,3,4,5]
# print(len(lst))
# print(sum(lst))
# print(max(lst))
# print(sorted(lst))

# a = 'Z'
# print(ord(a))

# a = 97
# print(chr(a))

# a='2' 를 정수 2로 바꾼 후 10을 더한 값을 출력

# a = '2'
# print(ord(a)-ord('0') + 10)

# a = -3
# print(abs(a))   # 절대값
# print(id(a))    # 주소값
# print(pow(3,2)) # 3의 2제곱

# import random
# a=[1,2,3,4,5,6,7]
# print(random.sample(a,2))

# memo={0:0,1:1}
# def fibonacci(n):
#     if n in memo:
#         return memo[n]
#     memo[n] = fibonacci(n-1)+fibonacci(n-2)
#     return memo[n]

# def getsum(a:int,b:int):    # tuple을 이용 값 두개 반환
#     return a+b,a*b


# ret=getsum(5,6)
# print(ret)
# print(type(ret))

# sum1=0
# gop1=0

# def getsum2(a,b):
#     global sum1,gop1
#     sum1=a+b
#     gop1=a*b

# getsum2(5,6)
# print(sum1, gop1)

# default Parameter랑 개수 맞추기
# default Parameter는 일반 parameter보다 항상 뒤에 와야한다

# def getsum(a,b=6,c=7):
#     return a+b+c

# ret=getsum(4)
# print(ret)

# num1=[1,2,3,4,5]
# num2=(1,2,3,4,5)
# print(num1,num2)

# a,b,c,d,e = num1
# print(a,b,c,d,e)
# a,b,c,d,e = num2
# print(a,b,c,d,e)

# 언패킹시 남는 값을 *을 사용하여 리스트!!!! 에 담을 수 있다.
# *은 아스트라스크, 아스트랄로 읽는다

# num = [1,2,3,4,5]
# num2=(1,2,3,4,5)
# a,b,*c = num
# print(c)
# a,b,*c = num2
# print(c)

# 함수의 매개변수 a에 들어는 parameter는 tuple로 받아짐
# def getsum(*a):     # 가변인자 사용해서 받으세요
#     sum = 0
#     print(a)
#     for i in a:
#         sum+=i
#     return sum

# result = getsum(1,2,3)
# print(result)


# def print_info(**args):
#     print(args)
#     for i,j in args.items():
#         print(i,j)

# print_info(kevin=1,john=2,bob=3)

# def print_info(**args):
#     print(args)
#     for i,j in args.items():
#         print(i,j)


# di={'kate':1,'amy':2,'kim':3}
# print_info(**di)

# map
# 리스트나 튜플같은 순회가능한 데이터 구조값들에
# 함수를 일괄적으로 적용하고
# 적용후 값을 map이라는 객체로 반환
# 사용법 map(함수,iterables)

num=[str(i) for i in range(1,4)]
lst1 = []
for i in num:
    lst1.append(int(i))
print(lst1)

# 맵 함수 이용시

lst2=map(int,num)
print(lst2)         # map이라는 함수 객체를 반환
print(list(lst2))   #리스트의 형태로 ㅏ꿔서 출력


lst1=[1,2,3]
lst2=[4,5,6]
# lst3 라는 리스트에 lst1 과 lst2의 합을 저장하는 리스트로 만든 후 출력

def fun2(a,b):
    return a+b
lst3=list(map(fun2,lst1,lst2))
print(lst3)