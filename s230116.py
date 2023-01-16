a = 3   # 3이라는 값을 가리키는 동적 할당 메모리의 주소값을 a에 저장(포인터라 생각해도 될 듯)
print(a, id(a))
b = a   # a의 주소값을 b에 저장
print(b, id(b))    # 따라서 a, b의 주소값이 같음

# 자료형
a = 3

print(type(a))
a = 3.14
print(type(a))
print(round(a,1))   # 소숫점 첫번쨰 까지만 출력
print(f'{a:.1f}')   # 소숫점 첫번쨰 까지만 출력

a = 5
a = str(a)  # 문자 '5'로 변환
print(a)
print(type(a))

print('오늘은 "100%"\n입니다')

# boolean
a,b = 0, -1
a, b = bool(a), bool(b)
print(a,b)

# 리스트
lst = [1,2,3,4,5]
print(lst)
print(type(lst))

print(lst[1]) # 2
print(len(lst)) # 리스트의 길이
print(lst[-1]) # 5

# 튜플
tp = (1,2,3,4,5)
print(tp)
print(type(tp))
print(len(tp))
print(tp[-1])