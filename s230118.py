# filter
# 리스트나 튜플과 같은 순회 가능한 데이터 구조 값들을 함수에 적용
# 적용 후 값중  True만 반환 ! filter라는 객체로 반환

# 리스트에서 짝수만
# num=[1,2,3,4,5]

# def get_even(t):
#     return True if t%2==0 else False

# result = filter(get_even,num)
# print(list(result))

# lambda
# 익명함수, 함수를 간략하게 적기 위해서 사용

# 숫자 두개 입력 받고 get_sum이라는 함수로 전달
# get_sum 함수에서 전달받은 두 수의 합을 리턴

# def get_sum(a,b):
#     return a+b

# a, b = map(int,input().split())
# print(get_sum(a,b))
# result = (lambda x,y:x+y)(a,b)
# print(result)

# # (lambda param1(,param2,...) : func)(arg1,...)

# sum2 = (lambda a,b:a+b)
# print(sum2(1,2))

# lst1 = [1,2,3,4,5]
# lst2 = [6,7,8,9,10]

# # 두 리스트 값들의 합을 lst3에 람다 함수를 사용하여 값을 채운 후 출력
# lst3 = list(map(lambda x,y:x+y, lst1,lst2))
# print(*lst3)

# lst = list(range(100))
# # 문제 : 리스트에서 짝수만 빼오기
# # filter, lambda 둘 모두 사용해서

# lst_even = list(filter(lambda even:even%2==0,lst))
# print(lst_even)

# 순환 가능한 데이터 구조에 일괄적용 = map
# 데이터에 일괄적용하는데 True 값만 따로 저장하겠다. => filter
# lambda 익명 함수 (사용자 함수를 직접 적지 않고 간단하게 함수 사용하고 싶을때)

# recursion
# 함수가 자기 자신을 계속 호출
# 1 2 3 4 5 6 7 8 9 10 9 8 7 6 5 4 3 2 1
# for i in range(1,4):
#     print(i, end=' ')
# for i in range(3,0,-1):
#     print(i, end=' ')
    
# print()
#########################

# def abc(level):
#     if level==4:
#         return
#     print(level,end=' ')
#     abc(level+1)
#     print(level,end=' ')
    
# abc(1)

# print()


# def abc(level):
#     print(level,end=' ')
#     if level==3:
#         print(level,end=' ')
#         return
#     abc(level+1)
#     print(level,end=' ')
# abc(1)

'''
문자열
리스트 튜플 딕셔너리 셋 관련 ㅁ메소드
copy(깊은복사 얕은복사)
'''

# st='apple,banana,mango'

# # 문자 'a'가 존재하는지 확인하고자 합니다.

# index=st.find('a',1)    # 없으면 -1 값 반환
# print(index)

# alpha=st.index('p') # 없으면 버그남
# print(alpha)

# # 대소문자 확인
# st='apple,banana,mango'
# print(st.isupper())
# print(st.islower())
# print(st.isalpha())

# print(st.count('a'))

# # join (합치기)
# st=['a','p','p','l','e']
# str2="".join(st)            # ""안에 구분자를 넣습니다.
# print(str2)

# #리스트 안에 문자를 합치는데 사이사이에 ,를 넣어라
# str2=','.join(st)
# print(str2)

# st=['apple','banana','mango']
# str2=','.join(st)
# print(str2)

# # 모두 대문자로 바꾸기
# # 모두 소문자로 바꾸기
# str2 = str2.upper()
# print(str2)
# str2 = str2.islower()
# print(str2)

# # 공백지우기 strip
# st='  apple   '
# str2 = st.strip()      # 오른쪽은 rstrip, 왼쪽은 lstrip
# print(str2)

# # 교체 replace
# str2 = st.replace('ap','mp')
# print(str2)

# # 리스트 값 추가
# st=['apple','banana','mango']
# st.append('orange')


# st.insert(1,'orange')       # 리스트 값을 중간 또는 맨앞에 추가할 때 사용

# print(st)

# st=[1,2,3]
# str2=[4,5]
# st.append(str2)
# print(st)

# st=[1,2,3]
# str2=[4,5]
# st.extend(str2)     # st+=str2 와 같음
# print(st)

# 리스트 값 지우기
# st = [1,2,3]
# st.pop()
# print(st)

# st=[1,2,3,4,1,2,3,4]
# st.remove(4)        # 처음 만나는 4를 삭제
# print(st)

# st=[1,2,3,4,1,2,3,4]
# del st[3:]
# print(st)

# # reverse
# st=[1,2,3,4,1,2,3,4]
# st.reverse()
# print(st)

# print(st[::-1])

# # sort
# a1=[6,3,9]
# print(a1)
# a1.sort()
# print(a1)

# a1 = sorted(a1,reverse=True)
# print(a1)

# a1=[6,3,9]
# ret = sorted(a1)        # 원본 데이터 값 유지 (sort와 다른점)
# print(a1,ret)
# ret = sorted(a1,reverse=True)

# # lambda를 이용한 sort

# lst = list(range(10))
# ret = sorted(lst, key=lambda x:x)   # ret = sorted(lst)
# print(ret)
# ret = sorted(lst,key=lambda x:x,reverse=True) #제대로된 내림차순 정리(문자건 숫자건 다 잘 작동)
# ret = sorted(lst, key=lambda x:-x)  # 내림차순 / 주의! 숫자만 가능 / 문자는 정렬 안됨
# print(ret)

# lst=[(1,'banana'),(2,'apple'),(3,'mango')]
# ret=sorted(lst,key=lambda x:x[1])
# print(ret)

# lst=[(1,'banana'),(2,'apple'),(3,'mango')]
# ret = sorted(lst, key=lambda x:x[0])
# print(ret)

# # lst=['banana','apple','mango']
# # 내림차순 / 주의! 숫자만 가능 / 문자는 정렬 안됨 / 오류발생
# # ret = sorted(lst, key=lambda x:-x)  
# # print(ret)

# # 딕셔너리
# st = {'kevin':1,'john':2,'bob':3}

# # 딕셔너리 (key랑 value) 추가하기
# st['kate']='hi'
# print(st)

# st['kevin']=11
# print(st)

# del st['kate']
# print(st)

# lst=st.keys()
# print(list(lst))

# lst=st.values()
# print(list(lst))

# lst=st.items()
# print(list(lst))        # 튜플의 형태로 (key,value) 반환

# # 딕셔너리 값 출력하기
# st={'kevin':1,'john':2,'bob':[1,2,3]}
# print(st.get('kevinn','없어요'))  # 키값을 받아올 떄 get을 이용하면 버그가 안남(없으면 default:None 반환)

# # 딕셔너리 값 정렬하기
# st={'kevin':27,'john':22,'bob':35}
# # 아이들의 나이가 적은 순으로 (오름차순) 정렬하기
# ret = dict(sorted(st.items(), key=lambda x:x[1]))
# print(ret)

# copy

# lst=[1,2,3]
# lst2=lst
# lst[0]=100
# print(*lst2)

###################

lst = [1,2,3]
# lst2 = lst.copy()     # 얕은복사
lst2 = lst[:]
lst[0]
print(lst2)

###################

lst=[[1,2],[3,4]]
lst2 = lst[:]           # copy() 얕은 복사 이후
lst[0][0] = 100
print(lst2[0][0])

###################
# 깊은 복사
import copy
lst=[[1,2],[3,4]]
lst2=copy.deepcopy(lst)
lst[0][0]=100
print(lst2[0][0])

##################

# 주소값을 찍어서 확인
a = 5
b = 5
print(id(a),id(b))
print()

lst=[1,2,3]
lst2=lst
print(id(lst),id(lst2))
print()

lst=[1,2,3]
lst2 = lst[:]
print(id(lst),id(lst2))
print()

lst=[[1,2],[3,4]]
lst2=lst[:]
print(id(lst),id(lst2))
print(id(lst[0]),id(lst2[0]))
print()



import copy
lst=[[1,2],[3,4]]
lst2 = copy.deepcopy(lst)
print(id(lst),id(lst2))
print(id(lst[0]),id(lst2[0]))
print()

words=['','','','']

x=[]
y=[]
for i in range(1,len(words)):
    if words[i-1][-1]!=words[i][0]:
        print(words[i])
        break
    
for i in range(0,len(words)):
    if i>0:
        if words[i-1][-1]!=words[i][0]:
            print(words[i])
            break
        
for i in words:
    if i not in x:
        x.append(i)
    else:
        if i not in y:
            y.append(i)
            break
print(y)