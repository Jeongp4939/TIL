""" 
# OOP : Object Oriented Programming
# 틀(class)을 만들어서 프로그래밍


class calculator():
    numberOfCalcul=0        # 클래스 변수 , 속성
    
    def __init__(self):     # 생성자 함수(constructor)
        self.result=0       # 인스턴스 변수
        calculator.numberOfCalcul+=1
        
    def getsum(self,value):
        self.result+=value
        return self.result

cal1 = calculator()           # 인스턴스, 클래스의 객체
# 인스턴스 변수? 인스터스가 개인적으로 가지고 있는 속성(attribute)
print(cal1.getsum(3))
print(cal1.getsum(4))
print(cal1.getsum(5))

cal2 = calculator()
print(cal2.getsum(6))
print(cal2.getsum(7))
print(cal2.getsum(1))

# 클래스 변수
# 한 클래스의 모든 인스턴스가 공유하는 값을 의미
print(cal1.numberOfCalcul)
print(cal2.numberOfCalcul)
print(calculator.numberOfCalcul)
# 클래스 변수 변경 시 주의 사항
# 클래스 변수 '값을 변경'시 항상
# 클래스.클래스변수 형식으로 변경해야함
calculator.numberOfCalcul=6
print(cal1.numberOfCalcul)
print(cal2.numberOfCalcul)
# 가능----------------------------------------
# 불가능--------------------------------------
cal1.numberOfCalcul=10
print(cal2.numberOfCalcul)  
# 이러면 안됨!(이것은 인스턴스 변수가 아님)
# numberOfCalcul은 모든 인스턴스가 공통으로 쓰는 값인데
# 인스턴스로 접근해서 마음대로 값을 바꾸면 안됨
# cal1.numberOfCalcul=10에서 새로운 인스턴스 변수가 생성됨

calculator.numberOfCalcul=20    # 문제가 발생
print(cal1.numberOfCalcul)      # 클래스 변수의 값을 바꿔도 이제 cal1은 바뀌지 않음
print(cal2.numberOfCalcul)

# 결론
# 클래스 변수: 모든 인스턴스가 공유,
#             인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
# 인스턴스 변수: 인스턴스 별러 독립되어 있음.
#              각 인스턴스가 값을 따로 저장해야 할 때 사용
"""
#===========================================
# [메서드]
# 1. 인스턴스 메서드
# 2. 클래스 메서드
# 3. 스태틱 메서드
#===========================================
""" 
# 자 이번에는 객체에 숫자 두개를 넣으면
# 두 수의 더한 값과 뺀 값을 돌려주는 클래스를 만들어 보자

# 1. 생성자 함수 없이 만들기
class plus_minus():
    # def data(self,first,second):    # 인자값으로 객체 a, 3,5를 뜻함
    #     self.first=first
    #     self.second=second
    
    def __init__(self,first,second) -> None:
        self.first=first
        self.second=second
    def plus(self):
        return self.first+self.second
    def minus(self):
        return self.first-self.second

a = plus_minus(3,5)
b = plus_minus(2,7)
print(a.first,b.second)

# 객체 a와 b는 각각 독립적이다
# 여기서 data가 바로 인스턴스 메서드이고
# 인스턴스 매서드는 self를 항상 첫번째 parameter로 사용
# 이름이 self일 필요는 없으나 관례적으로 self를 사용

print(a.plus())
print(b.minus())
 """
""" 
# __init__
# 매직 메서드(init, add, str 등) -> 인스턴스 생성하자 마자 자동 호출
# 특수한 메서드를 사용함으로써, 파이썬의 행위를 여러가지로 커스터마이즈 할 수 있다.
# 파이썬에서 문자열에서 + 연산자를 사용하면 두 문자열이 합쳐지는 것은
# 파이썬이라는 언어를 만들 때 문자열에 관한 클래스에 덧셈 연산이 되도록
# 클래스 안에 정의를 해 놓았기 떄문

# 실습
# 예를 들어 자동차를 생성하는 클래스를 만들고 자동차 가격의 합을
# 사용자가 쉽게 출력할 수 있도록 해보겠다

class car:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __add__(self,another):
        return self.price+another.price
    def __str__(self):
        return f'{kia.name}의 가격은 {kia.price}입니다.'

kia=car('k8',300)
bmw=car('m5',500)
# print(kia.price+bmw.price)
# print(kia+bmw)    # 커스터마이징 할 것, 지금 출력하면 버그

# add 라는 매직메서드를 커스터마이징 해서 덧셈 연산을 지원하도록 하겠다

print(kia+bmw)
# 이제 위와 같은 코드로 두 차량의 가격합 출력이 가능

# 다른 예를 하나 보자
# 우리가 print 함수를 사용하면 기본적으로 출력값으로 문자열 값을 반환하는데 이는
# print()메서드가 정의되어 있는 클래스 안에 __str__ 이라는 매직메서드가 있어서 이다.
# __str__매직메서드는 문자열을 반환해주는 메서드이다.

# 만약에 차이름과 가격을 동시에 출력한다면
print(f'{kia.name}의 가격은 {kia.price}입니다.')

# 그러나 나는 print(kia)라고 하면 위와 똑같이 출력하고자 한다. __str__ 메서드를 활용
print(kia)

del kia # 기아 인스턴스 삭제
print(kia)
"""

""" 
# 인스턴스를 통하지 않고 클래스에서 바로 호출 할 수 있는
# 스태틱(정적) 메서드, 클래스 메서드

# 데코레이터 : 장식하는 사람이라는 뜻
# 함수를 하나 만드는데 그 함수를 직접 수정하지 않고 함수에 기능을 추가하고자 할 때 사용

# 1. 먼저 데코레이터 사용 안한 예
# 이름과 나이를 출력 해 주는 각각의 함수를 정의

# def call_name(name):
#     print('*'*5)
#     print(name)
#     print('*'*5)

# def call_age(age):
#     print('*'*5)
#     print(age)
#     print('*'*5)

# def call_nickname(nick):
#     print('*'*5)
#     print(nick)
#     print('*'*5)
    
# call_name('박정훈')
# call_age(31)


# def deco(func):
#     def wrapping(value):
#         print('*'*8)
#         func(value)
#         print('*'*8)
#     return wrapping

# @deco
# def call_name(name):
#     print(name)

# @deco
# def call_age(age):
#     print(age)

# call_name('박정훈')
# call_age(31)

# 여기까지 데코레이터
 """
#================================================
""" 
# 정적 메소드

class car:
    @staticmethod
    def add_price(one,another):
        print(one+another)

# 정적 메소드에는 @staticmethod를 붙임
# self가 없다(self는 인스턴스 메소드에서 사용)
# add_price 함수의 매개변수를 넣는 데 self를 사용하지 않음

# car.add_price(400,800)

# 정적 메서드를 호출할 떄는 클래스에서 바로 메서드를 호출
# 클래스의 인스턴스가 없어도 문제 없음

# 다시 한번 말하지만 정적 메서드는 인스턴스 메서드처럼
# self를 받지 않습니다. 그래서 보통 정적 메서드는
# self와 같은 속성을 다루지 않고 단지

# 함수의 행동(기능)(메서드내용만) 하는 메서드를 클래스에 정의 할 떄 상ㅇ
# 그래서 호출 할 떄 클래스에서 바로 메서드를 호출

# 그러나 인스턴스가 있다면, 인스턴스로도 static method에 접근 가능
# 파이썬에서 가능(다른 언어는 안되는 경우가 많으므로 그냥 안쓰는게 좋음)
# a7=car()
# a7.add_price(500,600)

# 인스턴스로 정적메서드 호출은 잘 하지 않음
# 정적 메서드를 사용하는 이유

# 이 메서드는 클래스의 인스턴스에 어떠한 변화도 일으키지 않는 함수라는
# 의미를 내포하고 암시 할 때 사용

"""


# 클래스 메서드

# 몇명이 파이 만들었는지 확인하는 코드를 클래스 메서드를 사용해 보자

class make_pie:
    cnt=0
    def __init__(self,name):
        self.name=name
        make_pie.cnt+=1
    
    @classmethod
    def number_of_pies(cls):
        print(f'파이를 {cls.cnt} 명이 만들고 있습니다.')
    
    @classmethod
    def create(cls,name):   # class 내부에서 클래스 안에 있는 메서드를 호출하는 함수
        p=cls(name)
        return p

a=make_pie('kevin')
b=make_pie('jane')
c=make_pie('john')

# @classmethod 라는 데코레이터를 사용
# 호출시 첫번째 인자로 항상 cls를 사용
# cls는 클래스 자체를 의미하며 바로 make_pie를 뜻함

make_pie.number_of_pies()
make_pie.create('tom')
make_pie.create('bob')
make_pie.number_of_pies()








































