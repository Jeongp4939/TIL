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


# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# dic = {}

# for i in words:
#     if str(sorted(i)) not in dic:   # dic 안에 없으면 추가
#         dic[str(sorted(i))] = str(i)
#     elif str(sorted(i)) in dic:     # dic 안에 있으면 단어 추가
#         dic[str(sorted(i))] += ','+str(i)
# print(dic)
    

# print(locals())
# print(globals())


# 알파벳은 숫자보다 가치가 높다->한쪽만 알파벳이면 승리
# 알파벳 가치 J<Q<K<A
# 문양가치 spade>diamond>heart>clover

# def making_card_list() -> list:
# 	card_list = []

# 	for shape in ["spade", "heart", "diamond", "clover"]:

# 		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

# 			card_list.append((shape, number))

# 	return card_list


# trump_card_list = making_card_list()

# import random

# def card_game():
#     random.shuffle(trump_card_list)
#     card_cnt=len(trump_card_list)
#     cnt1, cnt2 =0,0
#     while cnt1<6 and cnt2<6:                                            # 둘 중 하나라도 6 이상이 되면 종료
#         Player1 = trump_card_list[random.randrange(0,card_cnt)]
#         trump_card_list.remove(Player1)
#         card_cnt-=1
#         Player2 = trump_card_list[random.randrange(0,card_cnt)]
#         trump_card_list.remove(Player2)
#         card_cnt-=1

        
#         if str(Player1[1]) == str(Player2[1]):                          # 문양이나 숫자가 같은 경우 먼저 확인
#             if Player1[0]=='spade' and Player2[0]!='spade':             # spade>diamond>heart>clover
#                 print(f'{Player1} {Player2} Player1 Win!')
#                 cnt1+=1
#             elif Player1[0]=='diamond' and Player2[0] not in ['spade']: # 카드의 중복은 없으므로 문자가 같을 때 다른것만 확인
#                 print(f'{Player1} {Player2} Player1 Win!')
#                 cnt1+=1
#             elif Player1[0]=='heart' and Player2[0] not in ['spade','diamond']:
#                 print(f'{Player1} {Player2} Player1 Win!')
#                 cnt1+=1
#             else:
#                 print(f'{Player1} {Player2} Player2 Win!')
#                 cnt2+=1
#         elif str(Player1[1]).isalpha() or str(Player2[1]).isalpha():
#             if str(Player1[1]).isalpha() and not str(Player2[1]).isalpha(): # 한명만 문자인 경우 승리
#                 print(f'{Player1} {Player2} Player1 Win!')
#                 cnt1+=1
#             elif not str(Player1[1]).isalpha() and str(Player2[1]).isalpha():
#                 print(f'{Player1} {Player2} Player2 Win!')
#                 cnt2+=1
#             elif str(Player1[1]) =='A' and str(Player2[1])!='A':            # 1이 A인 경우 2가 A가 아니면 1이 승리
#                 print(f'{Player1} {Player2} Player1 Win!')
#                 cnt1+=1
#             elif str(Player1[1]) =='K' and str(Player2[1]) not in ['A']:
#                 print(f'{Player1} {Player2} Player1 Win!')
#                 cnt1+=1
#             elif str(Player1[1]) =='Q' and str(Player2[1]) not in ['A','K']:
#                 print(f'{Player1} {Player2} Player1 Win!')
#                 cnt1+=1
#             else:
#                 print(f'{Player1} {Player2} Player2 Win!')
#                 cnt2+=1
#         else:                                                           # 둘 다 알파벳이 아닌 경우 숫자 비교
#             if Player1[1]>Player2[1]:
#                 print(f'{Player1} {Player2} Player1 Win!')
#                 cnt1+=1
#             elif Player2[1]>Player1[1]:
#                 print(f'{Player1} {Player2} Player2 Win!')
#                 cnt2+=1
#     print(f'{cnt1}:{cnt2} Finally plyer1 win') if cnt1>cnt2 else print(f'{cnt1}:{cnt2} Finally plyer2 win')

# card_game()



# calc 만들기

# import calc

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError:
#         print('0으로 나눌 수 없습니다.')

# print(calc.add(2, 3)) # 5
# print(calc.sub(2, 3)) # -1
# print(calc.mul(2, 3)) # 6
# print(calc.div(2, 3)) # 0.6666666666666666

# print(calc.div(2, 0)) # 0으로 나눌 수 없습니다.

# 입력 예시
# s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'

# 출력 예시
# 'I never dreamed about success, i worked for it.'

# new_s =''
# for ch in s:
#     if ch.isalpha() or ch in [' ',',','.']:
#         new_s+=ch
# new_s=new_s[0]+new_s[1:].lower()
# print(new_s)


# num_list = [4, 4, 7, 8, 10, 4]
# sum_of_repeat_number(num_list)

# 출력 예시 
#  25


# def sum_of_repeat_number(arr):
#     lst=[]
#     result = 0
#     while arr:
#         lst.append(arr.pop())
#         if lst[-1] in arr:
#             while lst[-1] in arr:
#                 arr.remove(lst[-1])
#             lst.pop()
#     while lst:
#         result+=lst.pop()
#     print(result)
        
        
# num_list = [4, 4, 7, 8, 10, 4]
# # num_list = list(map(int,input().split()))
# sum_of_repeat_number(num_list)


# words_dict = {'proper' : '적절한',
# 'possible' : '가능한',
# 'moral' : '도덕적인',
# 'patient' : '참을성 있는',
# 'balance' : '균형',
# 'perfect' : '완벽한',
# 'logical' : '논리적인',
# 'legal' : '합법적인',
# 'relevant' : '관련 있는',
# 'responsible' : '책임감 있는',
# 'regular' : '규칙적인'}

# def antonym(**kwargs):
#     words = list(kwargs.keys())
#     antonyms=[]
#     for word in words:
#         if word[0] in ['b','m','p']:
#             word = 'im'+ word
#         elif word[0] == 'l':
#             word = 'il'+word
#         elif word[0] == 'r':
#             word = 'ir'+word
#         else:
#             word = 'in'+word
#         antonyms.append(word)
    
#     return antonyms

# print(sorted(antonym(**words_dict),reverse=True))


# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
# 경고 월요일입니다.
# {'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

# import calendar

# def time_machine():
#     def year_ipt():
#         year = int(input())
#         if calendar.isleap(year):
#             print('윤년입니다. 연도를 다시 입력해 주세요')    
#             return year_ipt()
#         return year
#     year = year_ipt()
#     print(calendar.calendar(theyear=year))
#     day_of_week_lst = ['월요일','화요일','수요일','목요일','금요일','토요일','일요일']
#     month = int(input())
#     day = int(input())
#     day_of_week=day_of_week_lst[calendar.weekday(year,month,day)]
#     date_dic = {'년':year,'월':month,'일':day,'요일':day_of_week}
#     if date_dic['요일']=='월요일':
#         print('경고 월요일입니다.')
#     return date_dic
    
# print(time_machine())

generators={}

def fn_d(n):
    str_n = str(n)
    sum_n=0
    for i in str_n:
        sum_n+=int(i)
    return sum_n+n

def is_selfnumber(n):
    for i in range(1,n+1):
        generators[i] = fn_d(i)
    if n in generators.values():
        return False
    return True

n = int(input())
print(fn_d(n))
print(is_selfnumber(n))

