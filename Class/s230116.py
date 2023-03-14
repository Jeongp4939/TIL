# a = 3   # 3이라는 값을 가리키는 동적 할당 메모리의 주소값을 a에 저장(포인터라 생각해도 될 듯)
# print(a, id(a))
# b = a   # a의 주소값을 b에 저장
# print(b, id(b))    # 따라서 a, b의 주소값이 같음

# # 자료형
# a = 3

# print(type(a))
# a = 3.14
# print(type(a))
# print(round(a,1))   # 소숫점 첫번쨰 까지만 출력
# print(f'{a:.1f}')   # 소숫점 첫번쨰 까지만 출력

# a = 5
# a = str(a)  # 문자 '5'로 변환
# print(a)
# print(type(a))

# print('오늘은 "100%"\n입니다')

# # boolean
# a,b = 0, -1
# a, b = bool(a), bool(b)
# print(a,b)

# # 리스트
# lst = [1,2,3,4,5]
# print(lst)
# print(type(lst))

# print(lst[1]) # 2
# print(len(lst)) # 리스트의 길이
# print(lst[-1]) # 5

# # 튜플
# tp = (1,2,3,4,5)
# print(tp)
# print(type(tp))
# print(len(tp))
# print(tp[-1])

# N_post = int(input('게시글의 총 갯수를 입력하세요 : '))
# post_need = int(input('한 페이지에 필요한 게시글 수를 입력하세요 : '))

# if N_post%post_need>0:
#     print(f'{N_post//post_need+1}')
# else:
#     print(f'{N_post//post_need}')
    
# result = (a//b+bool(a%b))
# print(result)
# bool(a%b) 나누고 난 후 나머지가 0일 경우 False
# bool(a%b) 나누고 난 후 나머지가 0이 아닐 경우 True(1 반환)

# person1 = str(input())
# person2 = str(input())

# print(f'{person1}\n\n{person2}')

# N = int(input())
# result = 0
# for i in range(1,N):
#     if i%2 == 0 or i%7 ==0:
#         result += i
# print(result)

# m = 5
# n = 4

# for i in range(m):
#     print('*'*n)
# # print((('*'*n) + '\n')*m)

# score = {
#     'python': 80,
#     'django': 89,
#     'web': 83
# }

# score['algorithm'] = 90
# score['python'] = 85

# result = (sum(score.values())/len(score))
# print(result)

# s = input('숫자를 입력해주세요 : ')
# result = 0
# for i in str(s):
#     result+=int(i)
# print(result)

# s = {1,2,3,4,5}
# s.add(6)    # 한 개 추가
# print(s)
# s.update([11,12,8,7,6]) # 여러개 추가
# print(s)

# # 값 삭제
# s.remove(6) # 값 없으면 버그남!
# print(s)
# s.discard(13) # 삭제 하려고 하는 대상에 값이 없어도 버그 안남
# print(s)

# s.clear() # 다 삭제
# print(s)

# # 집합
# s1 = [1,2,3,4,5]
# s2 = [2,4,6,8]

# # 교집합
# s1, s2 = set(s1),set(s2)
# print(s1&s2)

# # 합집합
# print(s1|s2)
# print(s1.union(s2)) # union 함수 이용하는 법도 있음

# #차집합
# print(s1 - s2)

# a,b = map(int,input().split())
# print(a//b+bool(a%b))

# a = 3
# b = 6
# c = -5
# sol1 = round((-b-(b**2-4*a*c)**(1/2))/(2*a),3)
# sol2 = round((-b+(b**2-4*a*c)**(1/2))/(2*a),3)
# print((sol1,sol2))

# 입력 예시
# <p>취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.</p>

# 출력 예시
# 취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.

# str1 = input()
# replace_lst = ['<p>','</p>']
# for s in replace_lst:
#     str1 = str1.replace(s,'')

# print(str1)

# lst = []
# cnt = 0
# for _ in range(2):
#     lst.append(input())
# for i in range(min(len(lst[0]),len(lst[1]))):
#     if lst[0][i] == lst[1][i]:
#         cnt+=1
# print(max(len(lst[0][cnt:]),len(lst[1][cnt:])))
    
    
# case = int(input())
# box = []
# for _ in range(5):
#     box.append(list(map(int, input().split())))
# if case == 1:
#     for i in range(5):
#         print(*box[i][:i+1])
# else:
#     for i in range(5):
#         print(*box[i][:5-i])

# str1 = input()
# str2 = input()

# str_sum = sorted(list(str1))+sorted(list(str2))

# for s in str_sum:
#     print(s,end='')

# def fibonacci_reculsion(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1    
#     return fibonacci_reculsion(n-2) + fibonacci_reculsion(n-1)

# cache_list=[0,1]
# def fibonacci_lst_memoization(n):
#     cache_list=[0,1]
#     if n in cache_list:
#         return n
#     return fibonacci_lst_memoization(n-2) + fibonacci_lst_memoization(n-1)

# cache_dict={0:0, 1:1}
# def fibonacci_dict_memoization(n):
#     if n in cache_dict:
#         return cache_dict[n]
#     cache_dict[n] = fibonacci_dict_memoization(n-2) + fibonacci_dict_memoization(n-1)
#     return cache_dict[n]
# factorial_dict = {0:1,1:1}

# def factorial_memoization(n):
#     if n in factorial_dict:
#         return factorial_dict[n]
#     factorial_dict[n] = factorial_memoization(n-1) * n
#     return factorial_dict[n]

# def permutation(n, r):
#     return factorial_memoization(n)//factorial_memoization(n-r)
# def combination(n,r):
#     return permutation(n,r)//factorial_memoization(r)

# import time
# start= time.time()

# n,r = map(int,input().split())
# # print(fibonacci_reculsion(n))

# # end = time.time()
# # print(f'{end-start:.5f} sec')

# # start= time.time()

# # print(fibonacci_lst_memoization(n))

# # end = time.time()
# # print(f'{end-start:.5f} sec')

# start= time.time()
# # for i in range(1,n+1):
# #     print(fibonacci_dict_memoization(i))
# print(factorial_memoization(n))
# print(permutation(n,r))
# print(combination(n,r))

# end = time.time()
# print(f'{end-start:.5f} sec')


# lst = [0 for _ in range(9)]
# for _ in range(3):
#     n1, n2 = map(int, input().split())
#     for i in range(n1,n2+1):
#         lst[i] += 1
# print(*lst)

# lst_2 = [[5,1,4,2,6],[3,5,0,0,7],[9,9,8,3,1]]
# N = int(input())
# cnt = 0
# for i in lst_2:
#     for j in range(len(i)):
#         if i[j] > N:
#             cnt += 1
# print(f'{cnt}개')

# str_lst = input()
# str_lst = str_lst.upper()
# str1,str2,str3 = str_lst.split()
# if str1[-1] == str2[0] and str2[-1] == str3[0]:
#     print('pass')
# else:
#     print('fail')


# todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]

# work = input()
# day = int(input())

# todo.append((work,day))
# print(todo)

