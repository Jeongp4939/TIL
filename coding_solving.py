# orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
# orders = list(orders.split(','))

# order_set = list(set(orders))
# cnt = 0
# for i in order_set:
#     cnt += orders.count(i)
#     while i in orders:
#         orders.remove(i)
        
# print(f'총 {cnt}잔')
# print(sorted(order_set,reverse=True))


# orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
# orders = list(orders.split(','))

# order_set = list(set(orders))
# cnt = 0
# for i in orders:
#     if '아이스' in i:
#         cnt += 1
# print(f'아이스 음료 : 총 {cnt}잔\n')

# for i in order_set:
#     print(i, orders.count(i))
#     while i in orders:
#         orders.remove(i)
        
# fruit_pocket = input()
# fruit_pocket = fruit_pocket.lower()
# fruit_pocket = list(fruit_pocket.split(','))

# new_pocket = []
# for i in fruit_pocket:
#     if 'rotten' in i:
#         i = i.replace('rotten', '')
#         new_pocket.append(i)
#     else:
#         new_pocket.append(i)
# print(new_pocket)

# 문자열 중앙 문자 출력
# string=input()
# len_str = len(string)
# if len_str%2:
#     print(string[len_str//2])
# else:
#     print(string[len_str//2-1:len_str//2+1])

# 딕셔너리
# infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]
# result = 0
# for i in infos:
#     result+=i['age']
# print(result)

# blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
# blood_dict={'A':0,'B':0,'AB':0,'O':0}

# for i in blood_types:
#     blood_dict[i]+=1
    
# print(blood_dict)
        
# 소금물 문제

# salty_water=[]
# for i in range(5):
#     ipt = input()
#     if ipt=='Done':
#         break
#     else:
#         salty_water.append(tuple(map(int,ipt.split())))
# water = 0
# salt = 0
# for i in range(len(salty_water)):
#     water += salty_water[i][1]
#     salt += salty_water[i][0]*salty_water[i][1]/100
# print(round(salt/water*100,2))

# 윤년 판별
# n = int(input())
# if (n%4==0 and n%100!=0) or n%400==0:
#     print('윤년입니다.')
# else:
#     print('윤년이 아닙니다.')
    
# yyyy.mm.dd 로 입력 받을 경우
# date = input()
# y = int(date.split('.')[0])
# if (y%4==0 and y%100!=0) or y%400==0:
#     print('윤년입니다.')
# else:
#     print('윤년이 아닙니다.')


# 삼각형 종류 판별
# s_triangle=input()
# a, b, c = map(int,s_triangle.split())

# if a**2 > b**2+c**2 or b**2 > a**2+c**2 or c**2 > a**2+b**2:
#     print('삼각형이 아님')
# elif a==b==c:
#     print('정삼각형')
# elif a==b or b==c or c==a:
#     print('이등변 삼각형')
# elif a**2 == b**2+c**2 or b**2 == a**2+c**2 or c**2 == a**2+b**2:
#     print('직각삼각형')
# else:
#     print('삼각형')



# 비밀번호 입력(3회 실패시 종료)
# password='1234'
# for _ in range(3):
#     pw = input('비밀번호를 입력해 주세요 : ')
#     if pw == password:
#         print('맞았습니다.')
#         break

# 딕셔너리 생성

# students = ['박해피','이영희','조민지','조민지','김철수','이영희','이영희','김해킹','박해피','김철수',
#     '한케이','강디티','조민지','박해피','김철수','이영희','박해피','김해킹','박해피','한케이','강디티',]
# students_dic={}
# for i in students:
#     if i in students_dic:
#         students_dic[i]+=1
#     else:
#         students_dic[i]=0
# print(sorted(students_dic.items(),key=lambda item:item[1], reverse=True))



# # 입력 예시
# lst = [1, 1, 3, 3, 0, 1, 1]

# # 출력 예시
# # [1, 3, 0, 1]

# new_lst = []

# for i in lst:
#     if not new_lst:
#         new_lst.append(i)
#     if new_lst[-1]==i:
#         continue
#     else:
#         new_lst.append(i)
# print(new_lst)

# word1 = input()
# word2 = input()

# cnt1 = 0
# cnt2 = 0

# for w1 in word1:
#     cnt1+=ord(w1)
# for w2 in word2:
#     cnt2+=ord(w2)

# if cnt1>cnt2:
#     print(word1)
# else:
#     print(word2)

# test_status = {
#     '김싸피': 'solving',
#    	'이코딩': 'solving',
#    	'최이썬': 'cheating',
#    	'오디비': 'sleeping',
#    	'임온실': 'cheating',
#    	'조실습': 'solving',
#    	'박장고': 'sleeping',
#    	'염자바': 'cheating'
# }

# key_lst = list(test_status.keys())
# get_out = []

# for i in key_lst:
#     if test_status[i]=='solving':
#         continue
#     elif test_status[i]=='cheating':
#         get_out.append(i)
#         del test_status[i]
#     elif test_status[i]=='sleeping':
#         test_status[i] = 'solving'
# print(sorted(get_out))
# print(test_status)


# words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

# for i in range(1,len(words)):
#     if words[i-1][-1] != words[i][0] or words[i] in words[:i]:
#         print(f'{i+1}번째 사람')
#         break


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
dic = {}

for i in words:
    if str(sorted(i)) not in dic:   # dic 안에 없으면 추가
        dic[str(sorted(i))] = str(i)
    elif str(sorted(i)) in dic:     # dic 안에 있으면 단어 추가
        dic[str(sorted(i))] += ','+str(i)
print(dic)
    
        
            
            
        
    
            