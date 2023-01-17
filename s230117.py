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