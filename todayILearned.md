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
    - ```<``` 미만
    - ```<=``` 이하
    - ```>``` 초과
    - ```>=``` 이상
    - ```==``` 같음
    - ```!=``` 같지 않음
    - ```is``` 객체 아이덴티티(OOP)
    - ```is not``` 객체 아이덴티티가 아닌 경우

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
        - globals() 를 통해 확인 가능(dict)
    - local scope
        - 함수가 호출 될 때 생성되고, 함수가 종료될 때까지 유지
        - locals()를 통해 확인 가능(dict)
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

<details>
<summary> 23.01.19 </summary>

# **23.01.19**

<details>
<summary>함수 응용</summary>

## 함수 응용

<details>
<summary>내장 함수</summary>

### 내장 함수(Built-in Function)
- 파이썬 인터프리터에 내장된 항상 사용할 수 있는 함수와 형

#### map
- map(function, iterable)
    - 순회 가능한 데이터구조(itrable)의 모든 요소에 함수(funcion)를 정용하고, 결과를 map object로 반환
#### filter
- filter(function, iterable)
    - 순회가능한 데이터구조의 모든 요소에 함수를 적용하고, 그 결과가 True인 것들을 filter object로 반환
#### zip
- zip(*iterables)
    - 복수의 iterable을 모아 튜플을 원소로 하는 zip object 반환

#### lambda
- lambda [parameter]:표현식
    - 표현식을 계산한 결괏값을 반환하는 함수로, 이름이 없는 함수여서 익명함수라고도 불림
    - return 문을 가질 수 없음
    - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
    - 함수를 정의해서 사용하는 것보다 간결하게 사용 가능
    - def를 사용할 수 없는 곳에서도 사용가능
</details>

<details>
<summary>재귀 함수</summary>

### 재귀 함수(recursive function)
- 자기 자신을 호출하는 함수
- 무한한 호출을 목표로 하는것이 아니며, 알고리즘 설계 및 구현에서 유용하게 활용
    - 알고리즘 중 재귀 함수로 로직을 표현하기 쉬운 경우가 있음(ex> 점화식)
    - 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성
- 예시
    - Factorial
    - Fibonacci
#### 재귀 함수 주의 사항
- 재귀함수는 base case에 도달할 떄까지 함수를 호출함
- 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 동작하지 앟게 됨
- 파이썬에서는 최대 재귀 깊이가 1000번으로, 호출횟수가 넘어가면 Recursion Error가 발생

#### 반복문과 재귀함수 비교
- 알고리즘 자체가 재귀적인 표현이 자연스러운 경우 재귀함수를 사용
- 재귀 호출은 변수 사용을 줄여줄 수 있음
- 재귀 호출은 입력 값이 커질 수록 연산 속도가 오래 걸림

</details>
<details>
<summary>패킹/언패킹(Packing/Unpacking)</summary>

### 패킹/언패킹(Packing/Unpacking)
- 모든 시퀀스형(리스트,튜플 등)은 패킹/언패킹 연산자 *를 사용하여 객체의 패킹 또는 언패킹이 가능

#### 패킹
- 대입문의 좌변 변수에 위치
- 우변의 객체 수가 좌변의 변수 수보다 많을 경우 객체를 순서대로 대입
- 나머지 항목들은 모두 별 기호 표시된 변수에 <font color='purple'>리스트</font>로 대입

#### 언패킹
- argument 이름이 *로 시작하는 경우, argument unpacking 이라 함
    - *패킹의 경우, 리스트로 대입
    - *언패킹의 경우, 튜플 형태로 대입

#### 구분
- *연산자가 곱셈을 의미하는지 Packing/Unpacking 연산자인지 구분
    - Packing/Unpacking 연산자
        - *가 대입식의 좌측에 위치
        - *가 단항연산자로 사용
            - 단항 연산자: 하나의 항을 대상으로 연산이 이루어지는 연산자
    - 산술연산자로서의 *
        - *가 이항연산자로 사용되는 경우
            - 이항 연산자: 두 개의 항을 대상으로 연산이 이루어지는 연산자

</details>
<details>
<summary>가변인자</summary>

### 가변인자(*args)
- 가변인자
    - 여러개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
- 가변인자는 사용
    - 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용

#### Asterisk(*)와 가변 인자
- *는 시퀀스 언패킹 연산자라고 불리며, 말 그대로 시퀀스를 풀어헤치는 연산자
    - 주로 튜플이나 리스트를 언패킹하는데 사용
    - *를 활용하여 가변 인자를 만들 수 있음
    - 예시
    ```python
        def sum_all(*numbers):
            result = 0
            for number in numbers:
                result += number
            return result
    ```
    - 반드시 받아야 하는 인자와, 추가적인 인자를 구분해서 사용할 수 있음
    ```python
        def print_somthing(a, b, *c):
            print(f'a:{a}')
            print(f'b:{b}')
            print('c...')
            for i in c:
                print(f'c:{c}')
    ```
#### 가변 키워드 인자(**kwargs)
- 몇 개의 키워드 인자를 받을지 모르는 함수를 정의 할 떄 유용
- **kwargs는 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현
```python
    def family(**kwargs):
        for key, value in kwargs.items():
            print(key,":",value)
```
- 반드시 받아야하는 키워드 인자와, 추가적인 키워드 인자를 구분해서 사용 가능
- 가변 인자(*args)와 가변 키워드 인자(**kwargs)를 함께 사용할 수 있음

</details>
<details>
<summary>모듈과 패키지</summary>

## 모듈과 패키지
- 다양한 기능을 하나의 파일로 만든 것(module)
    - 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
- 다양한 파일을 하나의 폴더로 만든 것(package)
    - 특정 기능과 관련된 여러 모듈의 집합
    - 패키지 안에는 또 다른 서브 패키지를 포함
```python
    import module
    from module import var, function, Class
    from module import* # 전부 다 불러옴

    from package import module
    from package.module import var, function, Class
```
- 다양한 패키지를 하나의 묶음으로 만든 것(library)
- 관리하는 관리자(pip)
- 패키지의 활용 공간(가상환경)


### 파이썬 라이브러리
- 파이썬에 기본적으로 설치된 모듈과 내장 함수
- [라이브러리](https://docs.python.org/3.9/library/index.html)

#### 파이썬 패키지 관리자(pip)
- PyPI(Python Package Index)에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
- 패키지 설치
    - 최신 버전/특정 버전/ 최소버전을 명시하여 설치할 수 있음
    - 이미 설치되어 있는 경우 이미 설치되어 있음을 알리고 아무것도 하지 않음
    ```bash
        $ pip install SomePackage
        $ pip install SomePackage==1.0.5
        $ pip install SomePackage>=1.0.4
    ```
##### 명령어
- 패키지 삭제
    - $ pip uninstall SomePackage
- 패키지 목록 및 특정 패키지 정보
    - $ pip list
    - $ pip show SomePackage
- 패키지 관리하기
    - 아래의 명령어들을 통해 패키지 목록을 관리하고 설치할 수 있음
    - 일반적으로 패키지를 기록하는 파일의 이름은 requirements.txt로 정의
    ```
        $ pip freeze > requirements.txt
        $ pip install -r requirements.txt
    ```

### 모듈과 패키지의 활용
#### 패키지
- 패키지는 여러 모듈/하위 패키지로 구조화
    - Ex : package.module
- 모든 폴더에는 __init__.py를 만들어 패키지로 인식
    - Python 3.3 부터는 파일이 없어도 되지만, 하위 버전 호환 및 프레임워크 등에서의 동작을 위해 파일을 생성하는 것을 권장

### 가상환경
- 파이썬 표준 라이브러리가 아닌 외부 패키지와 모듈을 사용하는 경우 모두 pip를 통해 설치 해야 함
- 복수의 프로젝트를 하는 경우 버전이 상이할 수 있음
- 이러한 경우 가상환경을 만들어 프로젝트별로 독립적인 패키지를 관리 할 수 있음
- 가상환경을 만들고 관리하는데 사용되는 모듈(Python 버전 3.5부터)
- 특정 디렉토리에 가상 환경을 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음
    - 특정 폴더에 가상 환경이(패키지 집합 폴더 등) 있고
    - 실행 환경(ex-bash)에서 가상환경을 활성화 시켜 해당 폴더에 있는 패키지를 관리/사용함
- 가상환경을 생성하면 해당 디렉토리에 별도의 파이썬 패키지가 설치됨
    - $ python -m venv <폴더명>
- bash에서 $ source <venv>/bin/activate를 통해 활성화 가능
- 가상환경 비 활성화는 $ deactivate 명령어 사용

</details>
</details>
</details>

---

<details>
<summary> 23.01.25 </summary>

# **23.01.25**

## 데이터 구조
- 여러 데이터를 효과적으로 사용, 관리하기 위한 구조
- 파이썬의 대표적인 데이터 구조 : List,Tuple,Dict,Set 등

### 자료구조
- 컴퓨터 공학에서 '자료구조'라고 함
- 각 데이터의 효율적인 저장, 관리를 위한 구조를 나눠 놓은것

### 데이터 구조의 활용
- 데이터 구조를 활용하기 위해 메서드사용
    - 메서드는 클래스 내부에 정의한 함수, 사실상 함수와 동일
    - 쉽게 설명하면 객체의 기능

### 파이썬 공식 문서의 표기법
- python 구문이 아니며, 문법을 표현하기 위한 것
```python
str.replace(old,new[,count])
```
    - old, new는 필수 / [,count]는 선택적 인자를 의미

### 순서가 있는 데이터 구조

#### 문자열(String Type)
- 문자들의 나열(Sequence of characters)
    - 모든 문자는 str 타입(변경 불가능한 immuteable)
- 문자열은 작은 따옴표(')나 큰 따옴표(')를 활용하여 표기
    - 문자열을 묶을 때 동일한 문장부호를 활용
    - PEP8에서는 소스 코드 내에서 하나의 문장부호를 선택하여 유지하도록 함
##### 문자열 조회/탐색 및 검증 메서드
- s.find(x)     : 없으면, -1 반환
- s.index(x)    : 없으면, 오류
- s.isalpha()
- ...
- 문자열은 immutable(불변형)인데, 문자열 변경이 되는 이유
    - 기존의 문자열을 변경하는 게 아니라, 변경된 문자열을 새롭게 만들어서 반환
##### 문자열 변경
```python
.replace(old,new[,count])
```
- 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
- count를 지정하면, 해당 개수만큼만 시행

```python
.strip([chars])
```
- 특정한 문자들을 지정하면 제거(양쪽 / 왼쪽 lstrip / 오른쪽 rstrip)
- 문자열을 지정하지 않으면 공백을 제거함
```python
.split(sep=None, maxsplit=-1)
```
- 문자열을 특정한 단위로 나워 리스트로 반환
    - sep이 None이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주하고, 선행/후행 공백은 빈 문자열에 포함시키지 않음
    - maxsplit이 -1인 경우에는 제한이 없음
```python
'separator'.join([iterable])
```
- 반복가능한(iterable)컨테이너 요소들을 seperator(구분자)로 합쳐 문자열 반환
    -iterable에 문자열이 아닌 값이 있으면 TypeError 발생

#### 리스트
- 리스트는 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용

##### 리스트의 생성과 접근
- 리스트는 대괄호([]) 혹은 list()를 통해 생성
    - 파이썬에서는 어떠한 자료형도 저장할 수 있으며, 리스트 안에 리스트도 넣을 수 있음
    - 생성된 이후 내용 변경이 가능 -> 가변 자료형
    - 이러한 유연성 떄문에 파이썬에서 가장 흔히 사용
- 순서가 있는 시퀀스로 인덱스를 통해 접근 가능
    - 값에 대한접근은 list[i]
##### 값 추가 및 삭제
```python
.append(x)
```
- 리스트에 x 값을 추가함

```python
.insert(i,x)
```
- 정해진 위치 i에 x값을 추가

```python
.extend(iterable)
```
- 리스트에 iterable의 항목을 추가함

```python
.remove(x)
```
- 리스트에서 값이 x인 것 삭제/ 없으면 Value Error
```python
.pop(i)
```
- 정해진 위치 i에 있는 값을 삭제하고, 그 항복을 반환함
- i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함
```python
.clear()
```
- 모든 항목을 삭제
```python
.index(x)
```
- x 값을 찾아 해당 index값을 반환
```python
.count(x)
```
- 원하는 값의 개수를 반환
```python
.sort()
```
- 원본 리스트를 정렬함. None 반환
- sorted 함수와 구분
```python
.reverse()
```
- 순서를 반대로 뒤집음(정렬x)

#### 튜플
- 튜플은 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용
    - 리스트와의 차이점은 생성 후, 담고 있는 값 변경이 불가(불변 자료형)
- 항상 소괄호 형태로 사용
##### 튜플 관련 메서드
- 튜플은 변경할 수 없기 때문에 값에 영향을 미치지 않는 메서드만을 지원
- 리스트 메서드 중 항목을 변경하는 메서드들을 제외하고 대부분 동일

#### 연산자
##### 멤버십 연산자(Membership Operator)
- 멤버십 연산자 in을 통해 특정 요소가 속해 있는지 여부를 확인
- 포함 여부 확인
    - in
    - not in
- 산술연산자(+)
    - 시퀀스 간의 concatenation(연결/인쇄)
- 반복연산자(*)
    - 시퀀스를 반복


</details>


# **23.01.26**

## 데이터 구조
- 여러 데이터를 효과적으로 사용, 관리하기 위한 구조
- 파이썬의 대표적인 데이터 구조 : List,Tuple,Dict,Set 등

## 순서가 없는 데이터 구조

### 셋(set)
- set이란 중복되는 요소가 없이, 순서에 상관없는 데이터들의 묶음
    - 데이터의 중복을 허용하지 않음
    - 순서가 없기 때문에 인덱스를 이용한 접근이 불가능
- 수학에서의 집합을 표현한 컨테이너
    - 집합 연산이 가능(여집합을 표현하는 연산자는 별도로 존재X)
    - 중복된 값이 존재하지 않음
- 담고 있는 요소를 삽입 변경, 삭제가능 -> 가변 자료형(mutable)

##### 집합 관련 함수
```python
s.isdisjoint(t)
```
- 셋 s가 셋 t의 서로 같은 항목을 하나라도 갖고 있지 않은 경우, True반환(서로소)
```python
s.issubset(t)
```
- 셋 s가 셋 t의 하위 셋인 경우, True 반환
```python
s.issuperset(t)
```
- 셋 s가 셋 t의 상위 셋인 경우, True 반환

### 딕셔너리(Dictionary)
- 키-값(key-value) 쌍으로 이루어진 자료형
- Dictionary의 키(key)
    - key는 변경 불가능한 데이터(immutble)만 활용 가능
        - string, integer, float, boolean, tuple, range
    - 각 키의 값(values)
        - 어떠한 형태든 관계 없음

## 얕은 복사와 깊은 복사(Shaalow Copy & Deep Copy)
### 복사 방법

#### 할당
- 대입 연산자(=)
#### 얕은 복사(Shallow Copy)
- Slice 연산자 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사
- 복사하는 리스트의 원소가 주소를 참조하는 경우 주의
#### 깊은 복사(Deep Copy)
```python
import copy
a=[1,2,[3,4]]
b=copy.deepcopy(a)
```
- copy.deepcopy(a)를 이용

#### 결론
- 리스트를 복사하고 싶다면 무조건 print로 확인
- 디버깅 툴로 리스트 변화를 확인
- copy.deepcopy()를 항상 사용하면 메모리 용량이 증가하므로 필요한 경우만



# 23.01.30

## 객체 지향 프로그래밍(OOP: Object - Oriented Programming)
- 컴퓨터 프로그래밍의 패러다임 중 하나로, 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 여러개의 독립된 단위, 즉 '객체'들의 모임으로 파악하고자 하는 것
- 각각의 객체는 메시지를 주고받고, 데이터를 처리할 수 있다.

### 절차 지향 프로그래밍
- 프로그램 전체가 유기적인 흐름으로 연결
- 기능 중심의 프로그램
- 순서가 정해져 있으므로 실행이 빠름
#### But...
- 하드웨어가 발전함에 따라 소프트웨어도 점점 커지고 복잡한 설계가 요구됨 -> 하드웨어의 발전 속도를 소프트웨어의 발전속도가 따라가지 못함 -> 소프트웨어 의기(Software Crisis)
- 절차지향 방법론은 생산성이 낮으므로 '절차' 대신 핵심인 '데이터'를 중심으로 절차를 도입해서, 현실의 사물을 나타내고 조립하는 방식으로 개발하자 -> OOP

### 객체 지향 프로그래밍
- 프로그램을 여러 개의 독립된 객체들과 그 객체 간의 상호작용으로 파악하는 프로그래밍 방법

#### 객체 지향 프로그래밍이 필요한 이유
- 현실 세계를 프로그램 설계에 반영(추상화)

### 객체 지향의 장/단점
#### 장점
- 잘 만들어 놓으면 계속해서 재사용이 가능
- 객체는 그 자체로 데이터와 행동이 정의됨(독립적) -> 개발자가 내부 구조를 몰라도 그냥 가져와서 다른 객체와 조림하면서 개발 가능
- 객체 단위로 모듈화 시켜 개발할 수 있으므로 많은 인원이 참여하는 대규모 소프트웨어 개발 가능
- 개발 용이성, 유지보수 편의성, 신뢰성을 바탕으로 생산성이 높아짐

#### 단점
- 설계 시 많은 노력과 시간이 필요
    - 다양한 객체들의 상호 작용 구조를 만들기 위해 많은 시간과 노력이 필요
- 실행 속도가 상대적으로 느림
    - 절차 지향 프로그래밍이 컴퓨터의 처리구조와 비슷해서 실행 속도가 빠름

## OOP 기초
### 객체
- 컴퓨터 과학에서 객체 또는 오브젝트(Object)는 클래스에서 정의한 것을 토대로 메모리(실제 저장공간)에 할당 된 것
- 프로그래밍에서 사용되는 데이터 또는 식별자에 의해 참조되는 공간을 의미
- 변수, 자료구조, 함수 또는 메서드가 될 수 있음
-속성과 행동으로 구성된 모든 것

### 객체와 인스턴스
- 클래스로 만든 객체를 인스턴스 라고도 함
- 우리가 사용하는 데이터 타입이라는 것도 클래스
- 하나의 객체(Object)는 특정 타입의 인스터스(instance)

### 객체의 특징
- 타입(type): 어떤 연산자(operator)와 조작(method)이 가능한가
- 속성(attribute): 어떤 상태(데이터)를 가지는가
- 조작법(method): 어떤 행위(함수)를 할 수 있는가

## 객체와 클래스 문법
### 기본 분법
- 클래스 정의
```python
    class MyClass:
        pass
```
- 인스턴스 생성
```python
    my_instance=MyClass()
```
- 메서드 호출
```python
    my_instaxe.mymethod()
```
- 속성 접근
```python
    my_instance.my_attribute
```

### 클래스와 인스턴스
- 객체와 설계도(클래스)를 가지고, 객체(인스턴스)를 생성한다
- 클래스 : 객체들의 분류 / 설계도(class)
- 인스턴스 : 하나하나의 실체 / 예(instance)

#### 객체 비교하기
- ==
    - 동등한(equal)
    - 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
    - 두 객체가 같아 보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
- is
    - 동일한(ientical)
    - 두 변수가 동일한 객체를 가리키는 경우 True

#### 속성
- 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미
- 클래스 변수 / 인스턴스 변수가 존재

#### 인스턴스와 클래스 간의 이름공간(namespace)
- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면, 인스턴스 객체가 생성되고 이름 공간 생성
- 인스턴스에서 특정 속성에 접근하면, 인스턴스-클래스 순으로 탐색

#### 인스턴스 변수
- 인스턴스가 개인적으로 가지고 있는 속성(attribute)
- 각 인스턴스들의 고유한 변수
- 생성자 메서드(__init__)에서 self.<name>으로 정의
- 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당

#### 클래스 변수
- 한 클래스의 모든 인스턴스가 공유하는 값을 의미
- 같은 클래스의 인스턴스들은 같은 값을 갖게 됩
- 클래스 내부에서 정의
- <classname>.<name>으로 접근 및 할당

#### 클래스 변수 활용(사용핮 수 계산하기)
- 사용자가 몇 명인지 확인하고 싶다면
    - 인스턴스가 생성 될 때마다 클래스 변수가 늘어나도록 설정 가능
- 클래스 변수를 변경할 떄는 항상 클래스.클래스변수 형식으로 변경

## OOP 메서드
- 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)

### 메서드의 종류
- 인스턴스 메서드
- 클래스 메서드
- 정적 메서드

### 인스턴스 메서드
- 인스턴스 변수를 사용하거나, 인스턴스 변수 값을 설정하는 메서드
- 클래스 내부에 정의되는 메서드의 기본
- 호출 시, 첫 번째 인자로 인스턴스 자기자신(self)이 자동으로 전달됨
```python
class MyClass:
    def instance_method(self, arg1,...):
        pass
```

#### slef
- 인스턴스 자기자신
- 파이썬에서 인스턴스 메서드는 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
    - 매개변수 이름으로 self를 첫 번쨰 인자로 정의
    - 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙
#### 매직 메서드
- Double underscore(__)가 있는 메서드는 특수한 동작을 위해 만들어진 메서드로, 스페셜 혹은 매직 메서드라 불림
- 특정 상황에 자동으로 불리는 메서드
- 예
```python
__str__(self)       # 이 객체를 문자열로 표현하면 어떻게 표현할지 지정, print 함수 등에서 객체를 출력하면 자동으로 호출되는 메서드
__init__(self)      # 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
__it__(self,other)  
__le__(self,other)  
__eq__(self,other)  
__gt__(self,other)  # 부등호 연산자(>, greater than)
__go__(self,other)  
__ne__(self,other)  
```

### 클래스 메서드
- 클래스가 사용할 메서드
- @classmethod 데코레이터를 사용하여 정의
- 호출 시, 첫번 째 인자로 클래스(cls)가 전달 됨

#### 데코레이터
- 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
- @데코레이터(함수명) 형태로 함수 위에 작성
- 순서대로 적용되기 때문에 작성 순서가 중요

#### 클래스 메서드와 인스턴스 메서드
- 클래스 메서드 -> 클래스 변수 사용
- 인스턴스 메서드 -> 인스턴스 변수 사용
- 둘 모두 사용하고 싶다면
    - 클래스는 인스턴스 변수 사용이 불가능
    - 인스턴스 메서드는 클래스 변수, 인스턴스 변수 둘 다 사용 가능

### 스태틱 메서드
- 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메서드
- 속성을 다루지 않고, 단지 기능(행동) 만들 하는 메서드를 정의할 때 사용

- 인스턴스 변수, 클래스 변수 아무것도 사용하지 않을 경우 사용
    - 즉, 객체 상태나 클래스 상태를 수정할 수 없음
-@staticmethod 데코레이터를 사용하여 정의
- 일반 함수처럼 동작하지만, 클래스의 이름공간에 귀속됨
    - 주로 해당 클래스로 한정하는 용도로 사용

## 메서드 정리
- 인스턴스 메서드
    - 메서드를 호출한 인스턴스를 의미하는 self 매개 변수를 통해 인스턴스를 조작
- 클래스 메서드
    - 클래스를 의미하는 cls 매개 변수를 통해 클래스를 조작
- 스태틱 메서드
    - 클래스 변수나 인스턴스 변수를 사용하지 않는 경우에 사용
        - 객체 상태나 클래스 상태를 수정할 수 없음


# 23.01.31
## 객체 지향 프로그래밍
### 객체 지향의 핵심 개념
- 추상화
- 상속
- 다형성
- 캡슐화

### 추상화
- 현실세계를 프로그램 설계에 반영
    - 복잡한 것은 숨기고, 필요한 것만 드러냄

### 상속
- 두 클래스 사이 부모-자식 관계를 정립하는 것
- 클래스는 상속이 가능함
    - 모든 파이썬 클래스는 obejct를 상속 받음
    ```python
    class ChildClass(ParentClass):
    ```
- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음
- 부모 클래스의 속성, 메서드가 자식 클래스에 상속되므로, 코드 재사용성이 높아짐

#### 상속 관련 함수와 메서드
- ininstance(object, classinfo)
    - classinfo의 instance거나 subclass*인 경우 True
- issubclass(class, classinfo)
    - class가 classinfo의 subclass면 True
    - classinfo의 모든 항목을 검사
- super()
    - 자식클래스에서 부모클래스를 사용하고 싶은 경우
#### 상속 정리
- 파이썬의 모든 클래스는 object로부터 상속됨
- 부모 클래스의 모든 요소(속성, 메서드)가 상속됨
-  super()를 통해 부모 클래스의 요소를 호출할 수 있음
- 메서드 오버라이딩을 통해 자식 클래스에서 재정의 가능함
- 상속관계에서의 이름 공간은 인스턴스, 자식 클래스, 부모 클래스 순으로 탐색

#### 다중 상속
- 두 개 이상의 클래스를 상속 받는 경우
- 상속받은 모든 클래스의 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨

#### 상속 관련 함수와 메서드
- mro메서드 (Method Resolution Order)
    - 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
    - 기존의 인스턴스 -> 클래스 순으로 이름 공간을 탐색하는 과정에서 상속 관계에 있으면 인스턴스 -> 자식 클래스 -> 부모 클래스로 확장

### 다형성(Polymorphism)
- 여러 모양을 뜻하는 그리스어
- 동일한 메서드가 클래스에 따라 다르게 행동할 수 있음을 의미
- 즉, 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 다른 방식으로 응답할 수 있음

#### 메서드 오버라이딩
- 상속받은 메서드를 재정의
    - 클래스 상속 시, 부모 클래스에서 정의한 메서드를 자식 클래스에서 변경
    - 부모 클래스의 메서드 이름과 기본 기능은 그대로 사용하지만, 특정 기능을 바꾸고 싶을 때 사용
    - 상속받은 클래스에서 같은 이름의 메서드로 덮어씀
    - 부모 클래스의 메서드를 실행시키고 싶은 경우 super를 활용

### 캡슐화
- 객체의 일부 구현 내용에 대해 외부로부터의 직접적인 액세스를 차단
    - 예시 : 주민등록번호
- 파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음

### 접근 제어자 종류
- Public Access Modifier
    - Public Member
        - 언더바 없이 시작하는 메서드나 속성
        - 어디서나 호출이 가능, 하위 클래스 override 허용
        - 일반적으로 작성되는 메서드와 속성의 대다수 차지
- Protected Access Modifier
    - Protected Member
        - 언더바 1개로 시작하는 메서드나 속성
        - 암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능
        - 하위클래스 override 허용
- Private Access Modifier
    - Private Member
        - 언더바 2개로 시작하는 메서드나 속성
        - 본 클래스 내부에서만 사용이 가능
        - 하위 클래스 상속 및 호출 불가능(오류)
        - 외부 호출 불가능(오류)

### getter 메서드와 setter 메서드
- 변수에 접근할 수 있는 메서드를 별도로 생성
    - getter 메서드 : 변수의 값을 읽는 메서드
        - @property 데코레이터 사용
    - setter 메서드 : 변수의 값을 설정하는 성격의 메서드
        - @변수.setter 사용

## 에러와 예외처리
### 디버깅
- 최초의 버그는 1945년 프로그래밍 언어의 일종인 코볼 발명자 그레이스 호퍼가 발견
- 역사상 최초의 컴퓨터 버그는 Mark2 라는 컴퓨터 회로에 벌레인 나방이 들어가 합선을 일으켜 비정상적으로 동작
- 이때부터 소프트웨어에서 발생하는 문제를 버그라 부름

#### 디버깅의 정의
- 잘못된 프로그램을 수정하는 것을 디버깅이라 함 de(없애다)+bug(버그)
- 에러 메시지가 발생하는 경우
    - 해당 하는 위치를 찾아 메시지를 해결
- 로직 에러가 발생하는 경우
    - 명시적인 에러 메시지 없이 예상과 다른 결과가 나온 경우
        - 정상적으로 동작하였던 코드 이후 작성된 코드를 생각해봄
        - 전체 코드를 살펴봄
        - 휴식을 가져봄
        - 누군가에게 설명해봄
        - ...
```
코드의 상태를 신중하게 출력해가며 심사숙고 하는 것보다 효과적인 디버깅 도구는 없습니다. - 브라이언 커니핸, Unix for Beginners
```
- print 함수 사용
    - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
- 개발환경(text editor, IDE) 등에서 제공하는 기능 활용
    - breakpoint, 변수 조회 등
- python tutor 활용(단순 파이썬 코드인 경우)
- 뇌컴파일, 눈디버깅

### 에러와 예외
#### 문법 에러(Syntax Error)
- SyntaxError가 발생하면, 파이썬 프로그램은 실행이 되지 않음
- 파일이름, 줄번호, ^문자를 통해 파이썬이 코드를 읽어 나갈 떄(parser) 문제가 발생한 위치를 표현
- 줄에서 에러가 감지된 가장 앞의 위치를 가리키는 캐럿(caret)기호(^)를 표시
- Invaild systax
    - 문법 오류
- assign to literal
    - 잘못된 할당
- EOL(End of Line)
- EOF(End of File)

#### 예외(Exception)
- 실행 도중 예상치 못한 상황을 맞이하면, 프로그램 실행을 멈춤
    - 문자이나 표현식이 문법적으로 올바르더라도 발생하는 에서
- 실행 주에 감지되는 에러들을 예외(Exception)라고 부름
- 예외는 여러 타입(Type)으로 나타나고, 타입이 메시지의 일부로 출력됨
    - NameError, TypeError 등은 발생한 예외 타입의 종류(이름)
- 모든 내장 예외는 Exception Class를 상속받아 이뤄짐
- 사용자 정의 예외를 만들어 관리할 수 있음

##### 예외의 종류
- ZeroDivisionError
    - 0으로 나누고자 할 떄 발생
- NameError
    - namespace 상에 이름이 없는 경우
- TypeError
    - 타입 불일치
    - argument 누락
    - argument 개수 초과
    - argument type 불일치
- ValueError
    - 타입은 올바르나 값이 적절하지 않거나 없는 경우
- IndexError
    - 인덱스가 존재하지 않거나 범위를 벗어나는 경우
- KeyError
    - 해당 키가 존재하지 않는 경우
- ModuleNotFoundError
    - 찾는 모듈이 없는 경우
- ImportError
    - Module은 있으나 존재하지 않는 클래스/함수를 가져오는 경우
- keyboardInterrupt
    - 임의로 프로그램을 종료하였을 때
- IndentationError
    - Indentation이 적절하지 않는 경우(들여쓰기)

#### 예외처리
- try문(statement)/except절(clause)을 이용하여 예외처리를 할 수 있음
- try문
    - 오류가 발생할 가능성이 있는 코드를 실행
    - 예외가 발생되지 않으면, except 없이 실행 종료
    - try문은 반드시 한 개 이상의 except문 필요
- except 문
    - 예외가 발생하면, except 절이 실행
    - 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함
```python
try:
    try 명령문
except 예외그룹-1 as 변수-1:
    예외처리 명령문 1
except 예외그룹-2 as 변수-2:
    예외처리 명령문 2
finally:            #<-- 선택사항
    finally 명령문
```
- 에러 메시지 처리(as)
    - as 키워드를 활용하여 원본 에러 메시지를 사용할 수 있음
        - 예외를 다른 이름에 대입

#### 예외처리 종합
- try
    - 코드를 실행함
- except
    - try문에서 예외가 발생 시 실행함
- else
    - try 문에서 예외가 발생하지 않으면 실행함
- finally    
    - 예외 발생 여부와 관계없이 항상 실행함

- 파일을 열고 읽는 코드를 작성하는 경우
    - 파일 열기 시도
        - 파일이 없는 경우 -> '해당 파일이 없습니다.' 출력
        - 파일 있는 경우 -> 파일 내용을 출력
    - 해당 파일 읽기 작업 종료 메시지 출력




