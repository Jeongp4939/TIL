""" def emoji_decorator(func):
    def wrapper(name):
        func(name)
        print('^~^//')
    return wrapper

@emoji_decorator
def ko_hello(name):
    print(f'안녕하세요 {name}님!')
@emoji_decorator
def en_hello(name):
    print(f'Hello, {name}!')
    
def emoji_hello(name, func):
    func(name)
    print('^~^//')
    

ko_hello('name')
en_hello('name')

"""
""" 
class MyClass:
    
    def method(self):
        return 'instance medthod'
    
    @classmethod
    def class_method(cls):
        return 'class method'
    
    @staticmethod
    def static_method():
        return 'static method'
    
my_class = MyClass()
print(my_class.method())
print(my_class.class_method())
print(my_class.static_method())
"""
""" 
class Person:
    def __init__(self):
        self._age=0
        
    # def get_age(self):
    #     print('getter 호출')
    #     return self._age
    
    # def set_age(self,age):
    #     print('setter 호출')
    #     self._age=age
    
    @property
    def age(self):
        print('getter 호출')
        return self._age
    
    @age.setter
    def age(self,age):
        print('setter 호출')
        self._age=age
        
        
        
    # age = property(get_age, set_age)    # property를 이용하여 두 메서드를 사용 가능 age->class 변수
        
p1 = Person()
# p1._age = 25 # 오류는 안나지만 이럼 안됨
# print(p1._age) # 얘도 안됨

#불편함
# p1.set_age(25)
# print(p1.get_age())

p1.age = 25
print(p1.age)
"""
""" 
# 상속
# 기존에 있던 클래스(상위, 부모클래스)의 모든 속성과 메소드를
# 새로 만든 클래스 (하위, 자식클래스)가 그대로 물려받음으로써
# 코드의 재사용성이 높아짐

# 다시 한번 말해, 기존에 있는 클래스를 변경하지 않고
# 새로운 클래스에 기능을 추가하거나 변경할 떄 사용

class plus_minus:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def plus(self):
        result=self.first+self.second
        return result
    def minus(self):
        result=self.first+self.second
        return result
    


# 단 자식클래스에서 생성된 메서드를 부모클래스에서 사용은 불가능

# 메서드 오버라이딩
# 오버라이딩이란 덮어쓰기를 말함
# 부모클래스에 있는 메서드!!! 를 동일한 이름으로 자식클래스에서 다시 만드는 것
# 부모클래스의 메서드 이름과 기본기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 떄 사용

# 부모클래스에서 상속받은 plus의 메서드 기능에서
# 숫자 2개가 아닌 숫자 3개의 합이 100이 넘는다면
# '버그'라고 출력이 되도록
# 자식클래스에서 plus를 업그레이드 하려 한다고 가정


class morefunction(plus_minus):
    def __init__(self,first,second,third):
        super().__init__(first,second)
        self.third=third
        
    def mul(self):
        result=self.first*self.second*self.third
        return result
    
    def plus(self):
        get_sum = self.first+self.second+self.third
        if get_sum>100:
            print('버그')
        else:
            return print(get_sum)
    
    def parents_plus(self):
        return super().plus()
    

b=morefunction(3,4,98)
b.plus()

t = morefunction(500,300,200)
print(t.parents_plus())

# 이처럼 부모클래스의 plus 메서드를
# 새롭게 다시 정의하는 것을 '메서드 오버라이딩'이라고 한다
# 이번에는 자식 클래스에서 plus 메서드를 다시 정의 했지만
# 부모 클래스에서 plus 메서드를 자식클래스에서도 또 사용하고 싶다면
# 이떄 super()를 이용할 수 있다.


print(morefunction.mro())       # 상속의 구조를 확인하고자 할 때 쓰는 메서드


# 다중 상속

# 3. 객체지향의 핵심개념 (상속 추상화 캡슐화 다향성)
#     상속 : 부모클래스, 자식클래스 관계 → 속성과 메소드를 물려받아 사용 (super통해서 부모의 요소 호출가능)
#     추상화 : 복잡한것은 숨기고, 필요한 것 나타냄 (공통적인것은 부모클래스에 구현 개인 특성은 자식클래스에 구현)
#     캡슐화 : 객체 일부 구현 내용에 대해 외부로부터 직접적인 액세스 차단. (getter, setter)
#     다형성 : 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음. 메서드 (메서드 오버라이딩)
#     버그/예외처리
# '''


# 상속을 해보자
# 상속은 물려받다 라는 뜻으로 재산을 상속받다와 같은 의미다.
# 클래스를 하나 더 만드는데 원래 있던 클래스의 기능을 그대로 물려 받는 것이다.


# 기존에 있던 클래스 (상위,부모클래스)의 모든 속성과 메소드를 
# 새로 만든 클래스 (하위,자식클래스)가 그대로 물려 받음으로써
# 코드 재사용성이 높아짐

# 다시 한번 말하지만 기존에 있는 클래스를 변경하지 않고 새로운 클래스에
# 기능을 추가하거나 변경할때 사용한다.

class plus_minus:
    def __init__(self,first,second):
        self.first=first
        self.second=second       
    def plus(self):
        result=self.first+self.second
        return result
    def minus(self):
        result=self.first-self.second
        return result
# 위의 클래스는 숫자 2개의 합과 차를 반환하는 클래스 이다.

# 하위 클래스를 하나 만들 것임
# 부모클래스의 속성과 매소드 들이 자식클래스로 상속이 된다고 했음!!
# 숫자 3개의 곱을 구해주는 하위클래스를 만들꺼임

class morefunction(plus_minus):
    def __init__(self, first, second,third):
        super().__init__(first, second) # super는 부모클래스의 init메소드를 그대로 가져온 것
        self.third=third                # third만 추가
    def mul(self):
        result=self.first*self.second*self.third
        return result



# 단 자식클래스에서 생성된 메서드를 부모클래스에서 사용은 불가능 !!!


# 메서드 오버라이딩
# 오버라이딩이란 덮어쓰기를 말한다.
# 부모클래스에 있는 메서드!!! 를 동일한 이름으로 자식클래스에서 다시 만드는 것이다. 
# (부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용)

# 부모 클래스에서 상속받은 plus의 메소드의 기능에서
# 숫자 2개가 아닌 숫자 3개의 합이 100이 넘는다면 
# '버그' 라고 출력이 되도록
# 자식클래스에서 plus의 메소드 업그레이드 하려 한다고 가정하자


class morefunction(plus_minus):
    def __init__(self, first, second,third):
        super().__init__(first, second) # super는 부모클래스의 init메소드를 그대로 가져온 것
        self.third=third                # third만 추가
    def mul(self):
        result=self.first*self.second*self.third
        return result

    def plus(self):
        get_sum=self.first+self.second+self.third
        if get_sum>100:
            print('버그')
        else:
            return print(get_sum)
    
    def parents_plus(self):
        ret=super().plus()    # 부모 메서드에서의 plus메서드 호출시 super 활용 가능
        return ret
        

a=morefunction(1,1,99)
a.plus()
t=morefunction(500,400,200)
print(t.parents_plus())

print(morefunction.mro())


# 이처럼 부모클래스의 plus 메서드를 
# 새롭게 다시 정의하는 것을 "메서드 오버라이딩" 이라고 한다.
# 이번에는 자식클래스에서 plus 메서드를 다시 정의 했지만 (메서드 오버라이딩을 했지만)

# 부모 클래스에서의 plus 메서드를 자식클래스에서도 또 사용하고 싶다면!!
# 이때 super() 를 이용할 수 있다.

###################################

# 추상화
# 공통적으로 들어가는 속성과 메서드는 상위클래스에서 구현 해 주고
# 하위클래스에는 해당 클래스의 고유기능만 추가하는 것을 이론적으로 추상화라 한다.

###################################

# 다형성 : 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음. 
# 메서드 오버라이딩이 대표적인 예다.
# 상속받은 클래스에서 같은 이름으로 매서드를 덮어 씌울 수 도 있고
# 부모 클래스의 매서드를 사용하고 싶으면 super를 사용하기도 했다.
# 이처럼 동일한 메서드가 클래스에 따라 다르게 행동할 수 있다는 개념이 다형성이다.

###################################

# 캡슐화
# 객체의 일부 구현 내용을 외부에서 사용하지 못하게 차단하는 것
# 언제사용? 클래스 사용자가 클래스를 만든 개발자의 의도를 벗어나 
# 사용하는 것을 막기위해 접근을 제한함

# 개발자가 새로운 모듈을 만들었다. 그 모듈의 메서드를 사용하는데
# 공식문서에 사용법을 알려줘도 그대로 사용하지 않는것이 유저들이다.
# 그럼 개발자의 의도를 벗어나 사용하는 것을 막기위하여 또는 
# 특정 클래스 매서드 들의 접근을 막을떄 사용한다.


# 캡슐화를 통해 외부 접근을 제어하는데 3가지 가 있다.

#접근       제어자	문법의미

#Public	     name	외부로부터 모든 접근 허용
#Protected	_name	자기 클래스 내부 혹은 상속받은 자식 클래스에서만 접근 허용
#Private	__name	자기 클래스 내부의 메서드에서만 접근 허용

# public
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = 30

p1 = Person('김싸피', 30)

print(p1.name) # 김싸피
p1.age=40
print(p1.age) # 김싸피

# Person 클래스의 인스턴스인 p1은 이름(name)과 나이(age) 모두 접근 가능합니다.

# Protected
# 암묵적 규칙에 의해 메소드를 호출 시 
# 부모클래스 내부나 자식클래스에서만 호출이 가능하다
# 그러나 강제성은 없으므로 실제로는 Public과 거의 동일하게 외부 접근가능하다.
# (정말 막아주지는 않고 암묵적인 규칙)

class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age
    def getage(self):
        return self._age

p1 = Person('김싸피', 30)
print(p1.getage()) # 30
print(p1._age) # 30


#private

class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age      #언더스코어 2개를 붙여 
    def getage(self):
        return self.__age   #언더스코어 2개를 붙여 

p2=Person('아무개',30)
print(p2.name)
print(p2.__age)

# 이렇게 언더스코어(__) 2개를 통해 
# 클래스 멤버 속성을 외부에 있는 인스턴스로 직접 접근을 제한했습니다.
# 그래서 print(p2.__age) 라고 하면 속성을 직접적으로 출력이 안되었음

# getter 메소드와 setter 메소드를 만들어서 사용하면 가능하다.
# getter 메소드와 setter 메소드 는 
# 각각 property 그리고 setter라는 데코레이터를 사용한다.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age      #언더스코어 2개를 붙여 

    def getter(self):          # private한 속성값을 확인하고자 함 (getter함수가 됨)
        return self.__age
    
    def setter(self,value):    # private한 속성값을 변경하고자 함 (setter함수) 
        self.__age=value

k=Person('kevin', 39)
print(k.getter())
k.setter(29)
print(k.getter())

# 클래스의 private한 속성값을 getter와 setter를 이용해서 확인 그리고 값 변경이 가능함
# 그 다음에는 위 코드를 조금 더 간단하게 적기 위해 데코레이터를 사용할 것이다.

# getter 메소드에는 @property라는 데코레이터를 사용하고
# setter 메소드에는 @변수.setter 로 데코레이터를 사용할 것이다.

class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age
    
    @property                  # getter 함수 위에 @property라고 적어주고
    def age(self):           
        return self.__age
    
    @age.setter             # @메서드명.setter라고 적어준다
    def age(self,value):    
        self.__age=value

k=Person('kevin', 39)
print(k.age)
k.age=29
print(k.age)
# 참고로 @property 데코레이터 사용을 하면 메서드 호출시 ()를 생략해야 한다.
# 관례상 setter getter 함수명은 변수명을 따른다.


# 객체지향의 핵심개념 (상속 추상화 캡슐화 다향성) 상추캐다?
#     상속 : 부모클래스, 자식클래스 관계 → 속성과 메소드를 물려받아 사용 (super통해서 부모의 요소 호출가능)
#     추상화 : 복잡한것은 숨기고, 필요한 것 나타냄 (공통적인것은 부모클래스에 구현)
#     캡슐화 : 객체 일부 구현 내용에 대해 외부로부터 직접적인 액세스 차단. getter, setter.    
#     다형성 : 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음. 메서드 오버라이딩.
"""

from collections import Counter

lst = ['apple','mango','banana','apple','mango','mango','banana']

# counter 는 리스트 안에 중복된 데이터가 각각 몇개씩 있는지 알려줌
print(Counter(lst))

st = 'an apple mango'
ret = dict(Counter(st))
print(ret)
ret = sorted(ret.items(), key=lambda x:x[1],reverse=True)
print(ret[0])


st = 'an apple mango'
# st 요소를 세어, 최빈값 n개를 반환한다.
ret= Counter(st).most_common(n=2)
print(ret)

# 추가적으로 Counter를 가지고 덧셈 뺄셈도 지원
a = Counter('apple')
b = Counter('mango')
print(a+b)
print(a-b)

# 두 문자열을 대조할 떄에도 사용
a.subtract(b)
print(a)


