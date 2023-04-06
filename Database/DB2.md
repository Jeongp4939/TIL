---
jupyter:
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
  language_info:
    codemirror_mode:
      name: ipython
      version: 3
    file_extension: .py
    mimetype: text/x-python
    name: python
    nbconvert_exporter: python
    pygments_lexer: ipython3
    version: 3.9.12
  nbformat: 4
  nbformat_minor: 2
  orig_nbformat: 4
---

# DB 2일차

## Grouping data

Aggregate function

-   집계 함수
-   값 집합의 최대값, 최소값, 평균, 합계 및 개수를 계산
-   값 집합에 대한 계산을 수행하고 단일 값을 반환
    -   여러 행으로부터 하나의 결과 값을 반환하는 함수
-   SELECT 문의 GROUP BY 절과 함께 종종 사용됨
-   제공하는 함수 목록
    -   AVG(), COUNT(), MAX(), MIN(), SUM()
-   AVG(), MAX(), MIN(), SUM()는 숫자를 기준으로 계산이 되어져야 하기
    떄문에 반드시 컬럼의 데이터 타입이 숫자(INTEGER)일 때만 사용 가능

Aggregate function 예시

-   users 테이블의 전체 행 수 조회하기

``` sql
    SELECT COUNT(*) FROM users;
```

-   전체 유저의 평균 balance를 알고 싶다면

``` sql
    SELECT avg(balance) FROM users;
```

GROUP BY Clause

``` sql
    SELECT column_1, aggregate_function(column_2) FROM table_name
    GROUP BY column_1, column_2;
```

-   Make a set of sumary rows from a set of rows
-   특정 그룹으로 묶인 결과를 생성
-   선택된 컬럼 값을 기준으로 데이터(행)들의 공통 값을 묶어서 결과로
    나타냄
-   SELECT 문에서 선택적으로 사용가능한 절
-   SELECT 문의 FROM 절 뒤에 작성
    -   WHERE 절이 포함된 경우 WHERE 절 뒤에 작성해야 함
-   각 그룸에 대해 MIN, MAX, SUM, COUNT 또는 AVG와 같은 집계
    함수(aggregate function)를 적용하여 각 그룸에 대한 추가적인 정보
    제공 가능

Changeing data

-   데이터를 삽입, 수정, 삭제하기
    -   INSERT
    -   UPDATE
    -   DELETE

INSERT statement

``` sql
    INSERT INTO table_name(column1, column2,...)
    VALUES (value1, value2,...);
```

-   새 행을 테이블에 삽입
-   문법 규칙

1.  먼저 INSERT INTO 키워드 뒤에 데이터를 삽입할 테이블의 이름을 지정
2.  테이블 이름 뒤에 쉼표로 구분된 컬럼 목록을 추가
    -   컬럼 목록은 선택 사함이지만 컬럼 목록을 포함하는 것이 권장됨
3.  VALUES 키워드 뒤에 쉼표로 구분된 값 목록을 추가
    -   만약 컬럼 목록을 생략하는 경우 값 목록의 모든 컬럼에 대한 값을
        지정해야 함
    -   값 목록의 값 개수는 컬럼 목록의 컬럼 개수와 같아야 함

-   단일 행 삽입하기

``` sql
    INSERT INTO classmates(name, age, address)
    VALUES('홍길동',23,'서울');

    INSERT INTO classmates
    VALUES('홍길동',23,'서울');
```

여러행 삽입하기

``` sql
    INSERT INTO classmates
    VALUES
    ('김철수', 30, '경기'),
    ('이영미', 31, '강원'),
    ('박진성', 26, '전라'),
    ('최지수', 12, '충청'),
    ('정요한', 28, '경상');
```

`UPDATE` statement

``` sql
    UPDATE table_name
    SET column_1=new_value_1,
    column_2=new_value_2
    WHERE
    search_condition;
```

1.  UPDATE 절 이후에 업데이트할 테이블을 지정
2.  SET 절에서 테이블의 각 컬럼에 대해 새 값을 설정
3.  WHERE 절의 조건을 사용하여 업데이트할 행을 지정
    -   WHERE 절은 선택 사항.
    -   생략하면 UPDATE 문은 테이블의 모든 행에 있는 데이터를 업데이트
        함
4.  선택적으로 ORDER BY 및 LIMIT 절을 사용하여 업데이트 할 행 수를 지정
    할 수 있음

`DELETE` statement

``` sql
    DELETE FROM tabel_name
    WHERE search_condition;
```

-   테이블에서 행을 제거
-   테이블의 한 행, 여러 행 및 모든 행을 삭제할 수 있음
-   문법 규칙

1.  DELETE FROM 키워드 뒤에 행을 제거하려는 테이블의 이름을 지정
2.  WHERE 절에 검색조건을 추가하여 제거할 행을 식별
    -   WHERE 절은 선택 사항이며, 생략하면 DELETE 문은 테이블의 모든
        행을 삭제
3.  선택적으로 ORDER BY 및 LIMIT 절을 사용하여 삭제할 행 수를 지정 할
    수도 있음

### 정규형

데이터베이스 정규형

-   데이터베이스를 구조화 하는 방법론
-   데이터의 중복을 최소화하고 일관성과 무결성을 보장하기 위함
-   데이터의 구조를 더 좋은 구조로 바꾸는 것을 정규화라고 함
-   관계형 데이터베이스의 경우 6개의 정규형이 있음
-   제 1정규형, 제2 정규형, 제 3정규형만 살짝\...

제 1 정규형

-   하나의 속성값이 복수형을 가지면 안됨
-   하나의 속성에는 값이 하나만 들어가야함

제 2정규형

-   테이블에서 부분 함수적 종속성을 제거한 것

-   테이블의 기본키에 종속되지 않는 컬럼은 테이블이 분리 되어야함

-   테이블과 관련 없는 애들은 따로 분리하라는 것

-   Composite PK와 Partial Dependency를 키워드로 공부

제 3정규형

-   다른 속성에 의존(종속) 하는 속성은 따로 분리할 것
-   Transitive Dependency 키워드로 공부

JOIN

테이블은 여러 개로 나눠진다

-   테이블을 연결하는 것이 필요
-   JOIN(두 개 이상의 테이블에서 데이터를 가져와 결합하는 것)

CROSS JOIN

``` sql
    SELECT * FROM articles, users WHERE articles.userId = users.rowId;
    SELECT * FROM articles, users WHERE userId = users.rowId;-- 얘도 가능
```

INNER JOIN

``` sql
    SELECT * FROM articles, users WHERE articles.userId=users.rowid;
    SELECT * FROM articles INNER JOIN users
    ON userId=useres.rowId;
```

``` sql
    {테이블1} INNER JOIN {테이블2} ON {조건식}
```

#### 데이터는 일정하지 않다

LEFT (OUTER) JOIN

``` sql
    SELECT * FROM articles LEFT JOIN users
    ON userId=users.rowId;
```

``` sql
    SELECT * FROM articles RIGHT JOIN users
    ON userId=users.rowId;
```

## 정리

JOIN 두 개 이상의 테이블에서 데이터를 가져와 결합하는 것

-   `CROSS JOIN` 모든 조합 출력(잘 안씀)
-   `INNER JOIN` 두 테이블에서 일치하는 데이터만 결과 출력
-   `LEFT JOIN` 왼쪽 테이블의 데이터를 기준으로 오른쪽 데이터 결합,
    없으면 NULL
-   `RIGHT JOIN` LEFT와 반대
