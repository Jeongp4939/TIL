# **TIL(Today I Learned)**

## **목차**
---
<details>
<summary> 목차 </summary>

- [23.01.16](#230116)
    - [프로그래밍(Programming)](#프로그래밍programming)
        - [프로그래밍 언어란?](#프로그래밍-언어란)
    - [파이썬](#파이썬python)
        - [파이썬의 특징](#파이썬의-특징)
        - [파이썬 인터프리터](#파이썬python-인터프리터)
        - [파이썬 개발 환경 종류](#파이썬-개발-환경-종류)
    - [파이썬 기초문법](#파이썬-기초문법)
    - [변수와 식별자](#변수와-식별자)
    - [연산자](#연산자)
    - [자료형](#자료형)
    - [형 변환](#형-변환typecasting)
- [23.01.17](#230117)
    - [제어문](#제어문)
    - [코드 스타일 가이드](#코드-스타일-가이드)
    - [조건문](#조건문conditional-statement)
        - [복수 조건문](#복수-조건문)
        - [중첩 조건문](#중첩-조건문)
        - [조건 표현식](#조건-표현식conditional-expression)
    - [반복문](#반복문)
        - [반복문의 종류](#반복문의-종류)
            - [while 문](#while문)
            - [for 문](#for문)
        - [반복문 제어](#반복문-제어)
- [23.01.18](#230118)
    - [함수](#함수)
        - [함수 기초](#함수-기초)
            - [함수의 분류](#함수의-분류)
            - [함수의 정의](#함수의-정의)
        - [함수 기본 구조](#함수-기본-구조)
        - [선언과 호출(define&call)](#선언과-호출definecall)
        - [입력(input)](#입력input)
        - [문서화(Docstring)](#)
        - [범위(Scope)](#범위scope)
        - [결과값(Output)](#결과값output)



</details>

--- 

<details>
<summary> 23.01.16 </summary>

# **23.01.16**

<details>
<summary>프로그래밍</summary>

---
## **프로그래밍(Programming)**
- 컴퓨터에게 명령한느 적절한 수행 절차를 정의하고 이를 프로그래밍 언어로 표현하는 과정
    1. 컴퓨터에게 시키고 싶은 일을 정한다(계산, 저장 등)
    2. 컴퓨터가 이해할 수 있도록 수행 절차를 정의해서 표현
    3. 적절한 프로그래밍 언어를 선택하고, 언어를 이용해 절차를 기술
    4. 발생하는 오류를 수정(구문 오류(syntax error), 논리 오류(semantic error))
- [Computatuional Thinking](https://ko.wikipedia.org/wiki/%EC%BB%B4%ED%93%A8%ED%8C%85_%EC%82%AC%EA%B3%A0)이 중요
    1. 컴퓨터의 특성을 잘 이해한다.(understanding computer)
    2. 문제 해결 능력을 기른다.(problem solving / 논리적 사고 == 작은 문제로 쪼개기)
    3. 프로그래밍 언어에 능숙해진다.(trial & error)
    - **Just Do It**

    ###  **프로그래밍 언어란?**
    - 컴퓨터는 기계어로 소통함
    - 기계어는 사람이 이해하기 어렵기 때문에 기계어의 대안으로 사람이 이해할 수 있는 새로운 언어 개발
        - 사람이 이해할 수 있는 문자로 구성
        - 기본적인 규칙과 문법이 존재
    - 소스코드
        - 프로그래밍 언어로 작성된 프로그램
    - 번역기(interpreter 혹은 compiler)
        - 소스코드를 컴퓨터가 이해할 수 있는 기계어로 번역
        - 파이썬의 경우 인터프리터를 사용

</details>

<details>
<summary>파이썬</summary>

## **파이썬(python)**
### **파이썬의 특징**
- 다른 프로그래밍 언어에 비해 문법이 간단하며, 엄격하지 않음
- 별도의 데이터 타입 지정이 필요 없으며, 재할당이 가능
- 문장을 구분할 때 중괄호를 사용하지 않고 들여쓰기를 사용
- 소스코드를 기계어로 변환하는 컴파일 과정 없이 바로 실행 가능
- 객체 지향 프로그래밍 언어로 모든 것이 객체로 구현되어 있음

### **파이썬(Python) 인터프리터**
- 인터프리터 == 한 줄 씩 바로 실행할 수 있음
- 코드가 길어지면 한 줄 씩 입력하는 것은 무리가 있음
    - .py라는 확장자를 가진 파이썬 파일 작성
    - Git bash를 실행
    - cd desktop(엔터)
    - python {실행할 파이썬 파일 이름}.py

### **파이썬 개발 환경 종류**
- IDE(intergrated Development Environment)
    - 통합 개발 환경의 약자로 개발에 필요한 다양하고 강력한 기능들을 모아둔 프로그램
    - Ex) VScode, Pycharm
- Jupyter Notebook
- IDLE(Intergrated Development and Learning Environment)

</details>

<details>
<summary>파이썬 기초문법</summary>

## **파이썬 기초문법**

## **변수와 식별자**

### 변수(Variable)
- 데이터를 저장하기 위해 사용
- 변수를 사용하여 복잡한 값들을 쉽게 사용 가능(추상화)
- 동일 변수에 다른 데이터를 언제든 할당(저장) 가능
### 추상화
- 코드의 가독성 증가
- 숫자를 직접 적지 않고, 의미단위로 작성 가능
- 코드 수정이 용이해짐
### 변수의 할당
- 변수는 할당 연산자(=)를 통해 값을 할당(assignment)
- 값을 동시에 할당할 수 있음
    - a=b=1
    - -> a=1, b=1
- 다른값을 동시에 할당할 수 있음(Pythonic)
    - a, b = 1, 2
    - -> a=1, b=2
### 식별자(Identifiers)
- 변수의 이름을 식별자라고 함(변수, 함수, 클래스 ...)
- 읽기 쉽고 이해하기 쉬운 변수명이 최고
    - 변수명 짓기 사이트 존재
- 변수 이름 규칙
    - 식별자의 이름은 영문 알파벳, 언더스코거(_), 숫자로 구성
    - 첫 글자에 숫자가 올 수 없음
    - 길이 제한이 없고, 대소문자를 구별
        - 다음의 키워드(keywords)는 예약어(reserved words)로 사용할 수 없음
        - <font color='lightblue'>['False', 'None', 'True', '__peg_parser__', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']</font>
    - 내장 함수나 모듈 등의 이름을 사용하지 않아야 함
### 주석(Comment)
- 코드의 실행에 영향을 미치지 않는 메모 (파이썬은 #을 이용)
- 여러줄도 가능(""" 내용 """)
- <font color='#ffaaaa'>주석 다는 습관을 기르자</font>
- 주석 안달아 놓으면 까먹음

## 연산자
### 산술 연산자
- 기본적인 사칙연산 및 수식 계산
- '+', '-', '*', '/', '//', '**'
- 연산자 우선순위
    - 기본적으로 수학에서의 우선순위와 같음
    - 괄호가 가장 먼저 계산되고, 그 다음 곱하기(*)와 나누기(/)가 더하기(+) 뺴기(-) 보다 먼저 계산

### 비교 연산자
- 수학에서 등호와 부등호와 동일한 개념
- 주로 조건문에 사용되며 값을 비교할 떄 사용
- 결과는 True / False 값을 반환
    - < 미만
    - <= 이하
    - > 초과
    - >= 이상
    - == 같음
    - != 같지 않음
    - is 객체 아이덴티티(OOP)
    - is not 객체 아이덴티티가 아닌 경우

### 논리 연산자
- 여러 가지 조건이 있을 때
    - 모든 조건을 만족하거나(and), 여러 조건 중 하나만 만족해도 될 떄(or) 특정 코드를 실행하고 싶을 때 사용
    - 일반적으로 비교연산자와 함께 사용
        - A and B A,B 모두 True 일 때 True
        - A or B A와 B 모두 False일 때 False
        - not True를 False, False를 True
    - Falsy False는 아니지만 False로 취급 되는 다양한 값
        - 0, 0.0, (), [], {}, None, ""(빈 문자열)
    - 논리 연산자도 우선순위가 존재
        - not, and, or 순으로 우선순위가 높음(괄호 사용)
- 논리 연산자의 단축 평가
    - 결과가 확실한 경우 두번쨰 값은 확인하지 않고 첫번쨰 값 반환
    - and 연산에서 첫번째 값이 False인 경우 무조건 False -> 첫번째 값 반환
    - or 연산에서 첫번째 값이 True인 경우 무조건 True -> 첫번째 값 반환
    - 0은 False, 1은 True

## 자료형
### Data Type
- Boolean Type
- Numeric Type
    - Int
    - Float
    - Complex
- String Type
- 이외 list, tuple, dict, set ...

### 자료형과 메모리
1. 데이터를 저장할 공간을 만들고
2. 저장할 공간에 대한 주소를 할당
3. 할당 받은 주소를 기억했다가
4. 데이터를 해당 주소로 찾아가서 저장
5. 이후 데이터가 필요해지면 해당 주소로 가서 읽어온다
- 주소값을 기억하기가 어렵기 떄문에 메모리의 주소를 기억하는 이름으로 변수를 이용한다
- id()를 이용해 주소값을 확인 가능

### 자료형 분류
- 수치형(Numeric Type)
    - int(정수, integer)
    - float(부동소수점, 실수,floating point number)
    - complex(복소수, complex number)
- 문자열(String Type)
- 불린형(Boolean Type)
- None
- 하나로 모아서 list, tuple, range, dict, set ...

### 정수 자료형(int)
- 0, 100 ,-200 같은 정수를 표현
- 일반적인 수학 연산(사칙 연산) 가능

### 진수 표현
- 여러 진수 표현 가능
    - 2진수(Binary) : 0b
    - 8진수(Octal) : 0o
    - 16진수(heXadecimal) : 0x

### 실수 자료형(float)
- 유리수와 무리수를 포함하는 '실수'를 다루는 자료형
    - 0.1, 100.0, -0.001 등
- 부동 소수점
    - 실수의 값을 처리할 떄 의도하지 않은 값이 나올 수 있음
    - 컴퓨터는 2진수를 사용, 사람은 10진법을 사용하기에 컴퓨터는 10진법의 근사값만 표시
    - 이런 과정에서 예상치 못한 결과가 나타난다
- 해결책
    - 매우 작은 수보다 작은지 확인하거나, math 모듈을 활용

### 문자열 자료형
- 모든 문자는 str타입
- 문자열은 작은따옴표(')나 큰따옴표(")를 활용하여 표기
    - 문자열을 묶을 떄 동일한 문장부호를 활용
- 중첩 따옴표
    - 따옴표 안에 따옴표를 표현할 경우
        - 작은 따옴표 안에는 큰따옴표를
        - 큰 따옴표 안에는 작은 따옴표로 묶는다
- 삼중 따옴표(Triple Quotes)
    - 작은따옴표나 큰따옴표를 삼중으로 사용
        - 따옴표 안에 따옴표를 넣을떄
        - 여러 줄을 나눠 입력할 떄 편리
        ```python
        print('''한줄
        두줄
        세줄''')
        ```
- Escape Sequence
    - 역슬래시(backslash) 뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합(제어 시퀀스)
         - \n 줄바꿈
         - \t 탭
         - \r 캐리지 리턴
         - \o 널
         - \\ \
         - \' 단일인용부호(')
         - \" 이중인용부호(")
- 문자열 연산
    - 덧셈 : 문자열 덧샘은 연결
    - 곱셈 : 문자열 반복

### None
- 파이썬 자료형 중 하나
- 값이 없음을 표현하기 위해 None 타입 존재
- 일반적으로 반환 값이 없는 함수에서 사용

### 불린형(Boolean)
- 논리 자료형으로 참과 거짓을 표현
- True 또는 False를 값으로 가짐
- 비교 / 논리 연산에서 활용됨

### 컨테이너
- 여러 개의 값(데이터)을 담을 수 있는 것(객체)으로, 서로 다른 자료형을 저장할 수 있음 ex)List
- 컨테이너의 분류
    - 순서가 있는 데이터(Ordered) vs 순서가 없는 데이터(Unordered)
    - 순서가 있다 != 정렬되어 있다
- 컨테이너
    - 시퀀스형
        - 리스트(mutable, []), tuple(immutable, ()), range(immutable, range())
    - 비시퀀스형
        - 세트(mutable, {}), 딕셔너리(mutable, {key:value})
## 형 변환(Typecasting)
- 데이터 형태는 서로 변환할 수 있음
- 암시적 형 변환(Implicit)
    - 사용자가 의도하지 않고, 파이썬 내부적으로 자료형을 변환하는 경우
    - bool
    - Numeric type(int, float)
- 명시적 형 변환(Explicit)
    - 사용자가 특정 함수를 활용하여 의도적으로 자료형을 변환하는 경우
    - str,float -> int
    - str,int -> float
    - int,float,list,tuple,dict -> str
- 컨테이너 간의 형 변환

```markdown
    
    | - | string | list | tuple | range | set |
    | - | O | O | X | O | X |
    | O | - | O | X | O | X |
    | O | O | - | X | O | X |
    | O | O | O | - | O | X |
    | O | O | O | X | - | X |
    | O | O | O | X | O | X |

```

</details>
</details>


---

<details>
<summary>23.01.17</summary>

# **23.01.17**

<details>
<summary>제어문</summary>

## **제어문**
- 순차, 선택, 반복
- 파이썬은 기본적으로 위에서부터 아래로 차례대로 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건) 하거나 계속하여 실행(반복)하는 제어가 필요
- 제어문은 순서도(flowchart)로 표현 가능

## 코드 스타일 가이드
- Space Sensitive
    - 문장을 구분할 때, 중괄호 ({,}) 대신 들여쓰기(indentation)를 사용
    - 들여쓰기를 할 떄는 4칸(space키 4번) 혹은 1탭(Tab키 1번)을 입력
        - <font color='red'>주의!</font> 한 코드 안에서는 반드시 한 종류의 들여쓰기를 사용
    - Tab으로 들여쓰면 계속 탭으로 들여써야 함
    - 원칙적으로 공백(빈칸, space) 사용을 권장 *PEP8 권장사항

</details>

<details>
<summary>조건문</summary>

## **조건문(Conditional Statement)**
- 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용
- 조건에는 참/거짓에 대한 조건식
    - 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블록을 실행
    - 이외의 경우 else 이후 들여쓰기 되어있는 코드 블록을 실행
        - else는 선택적으로 활용할 수 있음
    ``` python
    a = 5
    if a>5:
        print('5 초과')
    else:
        print('5 이하')
    print(a)
    ```
### **복수 조건문**
    - 복수의 조건식을 활용할 경우 elif를 활용하여 표현함
### **중첩 조건문**
    - 조건문은 다른 조건문에 중첩되어 사용될 수 있음
        - 들여쓰기에 유의하여 작성할 것
#### **조건 표현식(Conditional Expression)**
    - 조건 표현식을 일반적으로 조건에 따라 값을 정할 떄 활용
    - 삼항 연산자(Ternary Operator)로 부르기도 함
    - ex) (true인 경우 값) if [조건] else (false인 경우 값)
    ```python
    value = num if num>=0 else -num
    # 절대값을 저장하기 위한 코드
    ```
    ```python
    result='홀수입니다' if num%2 else '짝수입니다'
    # 짝수 홀수 판단
    ```

</details>

<details>
<summary>반복문</summary>

## **반복문**

- 특정 조건을 만족할 때까지 동작을 계속 반복하고 싶을 때 사용
### 반복문의 종류
- while문
    - 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
- for 문
    - 반복 가능한 객체를 모두 순회하면 종료(별도의 종료 조건이 필요 없음)
- 반복 제어
    - break, continue, for-else
#### while문
- while문은 조건식이 참인 경우 반복적으로 코드를 실행
    - 조건이 참인 경우 들여쓰기 되어 있는 코드블록 실행
    - 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행
    - while문은 무한 루프를 하지 않도록 종료 조건이 반드시 필요
    ```python
    a = 0
    while a<5:
        print('a')
        a += 1
    print('끝')
    ```
- 복합 연산자(In-Place Operator)
    - 복합 연산자는 연산과 할당을 합쳐놓은 것

#### for문
- for문은 시퀀스(sring, tuple, list, range)를 포함한 순회 가능한 객체(iterable)의 요소를 모두 순회
    - 처음부터 끝까지 모두 순회하므로 별도의 종료 조건이 불필요
- iterable
    - 순회할 수 있는 자료형(sring, list, dict, tuple, range, set 등)
    - 순회형 함수(range, enumerate)
```python
fruit_box = ['banana','apple','mango']
for fruit in fruit_box:
    print(fruit)
print('끝')
```
- List Comprehension
    - 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성
```python
[code for 변수 in iterable]
[code for 변수 in iterable if 조건식]
```

- Dictionary Comprehension
    - 표현식과 제어문을 통해 특정한 값을 가진 딕셔너리를 간결하게 생성
```python
{key:value for 변수 in iterable}
{key:value for 변수 in iterable if 조건식}
```
### 반복문 제어
- break
    - 반복문을 종료
- continue
    - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
- for-else
    - 끝까지 반복문을 실행한 이후에 else문 실행
    - break를 통해 중간에 종료되는 경우 else문은  실행되지 않음
- pass
    - 아무것도 하지 않음(문법적으로 필요하지만, 할 일이 없을 때 사용)

</details>

</details>

---

<details>
<summary>23.01.18</summary>

# **23.01.18**

<details>
<summary>함수</summary>

## **함수**
---
- 함수의 사용 이유
    - 분해(Decomposition)
        - 기능을 분해하고 재사용 가능하게 만듬
    - 추상화(Abstraction)
        - 복잡한 내용을 모르더라도 사용할수 있게 만듬
        - 재사용성과 가독성, 생산성을 늘림
        - 내부 구조를 변경할게 아니라면 몰라도 됨

<details>
<summary>함수 기초</summary>

## 함수 기초
---

### 함수의 분류
- 내장 함수
    - 파이썬에 기본적으로 포함된 함수
- 외장함수
    - import 문을 통해 사용하며, 외부 라이브러리에서 제공하는 함수
- 사용자 정의 함수
    - 사용자가 직접 만드는 함수
### 함수의 정의
- 특정한 기능을 하는 코드의 조각(묶음)
- 특정 코드를 매번 다시 작성하지 않고, 필요시에만 호출하여 간편히 사용

</details>

<details>
<summary>함수 기본 구조</summary>

## 함수 기본 구조
- 선언과 호출(define&call)
- 입력(input)
- 문서화(Docstring)
- 범위(Scope)
- 결과값(Output)

### **선언과 호출(define&call)**
- 함수의 선언은 def 키워드 활용
- 함수명()으로 호출 / Parameter가 있는 경우 함수명(값1, 값2,...)으로 호출
- 들여쓰기를 통해 Function body(실행될 코드 블록) wkrtjd
    - Docstring은 함수 body 앞에 선택적으로 작성 가능
    - 작성 시에는 반드시 첫번쨰 문장에 문자열 """
- 함수는 Parameter를 넘겨줄 수 있음
- 함수는 동작 후에 return을 통해 결과값을 전달

### 입력(input)
#### Parameter와 Argument
- Parameter
    - 함수를 정의 할 때, 함수 내부에서 사용되는 변수
- Argument
    - 함수를 호출 시 함수의 parameter를 통해 전달 되는 값
    - Argument는 소괄호 안에 할당 func_name(argument)
        - 필수 Argument: 반드시 전달 되어야 하는 argument
        - 선택 Argument: 값을 전달하지 않아도 되는 경우는 기본값이 전달
    - Positional Arguments
        - 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨
        - 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
        - Keyword Argument 다음에 Positional Argument를 활용할 수 없음
        ``` python
            def add(x,y):
                return x + y
            
            add(x=2, y=5)
            add(2, y=5)
            add(x=2, 5) # -> Error 발생함

        ```
    - Defaul Arguments Values
        - 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
        - 정의된 것 보다 더 적은 개수의 argument들로 호출 될 수 있음
```python
    def function(ham):  # parameter : ham
        return ham
    function('spam')    # argument : 'spam'
    # 함수 리턴값 : spam
```


### 범위(Scope)
- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
#### scope
- global scope
    - 코드 어디에서든 참조할 수 있는 공간
- local scope
    - 함수가 만든 scope. 함수 내에서만 참조 가능
#### variable
- global variable
    - global scope에 정의된 변수
- local variable
    - local scope에 정의된 변수
#### 변수 수명주기(lifecycle)
- 변수는 각자의 수명주기(life-cycle)가 존재
    - built-in scope
        - 파이썬이 실행된 이후부터 영원히 유지
    - global scope
        - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
    - local scope
        - 함수가 호출 될 때 생성되고, 함수가 종료될 때까지 유지
#### 이름 검색 규칙(Name Resolution)
- 파이썬에서 사용되는 이름(식별자)들은 이름공간(namespace)에 저장되어 있음
- 아래와 같은 순서로 이름을 찾아나가며, LEGB Rule 이라고 부름
    - Localscope : 지역 범위(현재 작업 중인 범위)
    - Enclosed scope : 지역 범위 한 단계 위 범위
    - Global scope : 최상단에 위치한 범위
    - Built-in scope : 모든 것을 담고 있는 범위(정의하지 않고 사용 가능)
- 함수 내에서는 바깥 Scope의 변수에 접근 가능하나 수정은 할 수 없음
#### global 문
- 현재 코드 블록 전체에 적용되며, 나열된 식별자(이름)이 global varibable임을 나타냄
    - global에 나열된 이름은 같은 코드 블록에서 global 앞에 등장할 수 없음
    - global에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
#### nonlocal
- global을 제외하고 가장 가까운(둘러싸고 있는) scope의 변수를 연결하도록 함
    - nonlocal에 나열된 이름은 같은 코드 블로에서 nonlocal 앞에 등장할 수 없음
    - nonlocal에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
- global과는 달리 이미 존재하는 이름과의 연결만 가능
#### <font color='red'>함수의 범위 주의</font>
- 기본적으로 함수에서 선언된 변수는 Local scope에 생성되며, 함수 종료시 사라짐
- 해당 scope에 변수가 없는 경우 LEGB rule에 의해 이름을 검색
    - 변수에 접근은 가능하지만, 해당 변수를 수정할 수 없음
    - 값을 할당하는 경우 해당 scope의 이름 공간에 새롭게 생성
    - 단, 함수 내에서 피요한 상위 scope 변수는 argument로 넘겨서 활용할 것
- 상위 scope에 있는 변수를 수정하고 싶다면 global, nonlocal 키워드를 활용 가능
    - 단, 코드가 복잡해 지면 변수의 변경을 추적하기 어렵고, 예기치 못한 오류 발생
    - 가급적 사용하지 않는 것을 권장하며, 함수로 값을 바꾸고자 한다면 항상 argument로 넘기고 리턴값을 사용 하는 것을 추천

### 결과값(Output)
- Void function
    - 명시적인 return 값이 없는 경우, None을 반환하고 종료
- Value returning function
    - 함수 실행 후, return문을 통해 값 반환
    - return 하게 되면, 값 반환 후 함수가 바로 종료
        - return은 항상 하나의 값 만을 반환
        - 튜플을 활용하여 두개 이상의 값을 반환 가능
    ```python
        # void function 예시
        def void_product(x,y):
            print(f'{x}x{y}={x*y}')
        void_product(4,5)   # 4 x 5 = 20
        ans = void_product(4, 5)
        print(ans) # None
    ```
    ```python
        # Value returning function 예시
        def value_returning_product(x,y)
            return x*y
        value_returning_product(4,5)
        ans = value_returning_product(4,5)
        print(ans) # 20
    ```


</details>
</details>

</details>

---