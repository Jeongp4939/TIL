### 3월에 태어난 여성 회원 목록 출력하기
```sql
    SELECT MEMBER_ID, MEMBER_NAME, GENDER, DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH --DATE_FORMAT({date_data},{date_data 형태}) AS {DATA Column name}
    FROM MEMBER_PROFILE
    WHERE (MONTH(DATE_OF_BIRTH) = 3) AND (GENDER = 'W') AND (TLNO IS NOT NULL)
    ORDER BY MEMBER_ID ASC
```

### 과일로 만든 아이스크림 고르기
```sql
    SELECT A.FLAVOR
    FROM FIRST_HALF A JOIN ICECREAM_INFO B ON A.FLAVOR = B.FLAVOR
    WHERE TOTAL_ORDER > 3000 AND INGREDIENT_TYPE = 'fruit_based'
    ORDER BY TOTAL_ORDER DESC
```

### 12세 이하인 여자 환자 목록 출력하기
```sql
    SELECT PT_NAME, PT_NO, GEND_CD, AGE, ifnull(TLNO,'NONE') AS TLNO
    FROM PATIENT
    WHERE GEND_CD='W' AND AGE <= 12
    ORDER BY AGE DESC, PT_NAME
```

### 흉부외과 또는 일반외과 의사 목록 출력하기
```sql
    SELECT DR_NAME, DR_ID, MCDP_CD, DATE_FORMAT(HIRE_YMD, '%Y-%m-%d') AS HIRE_YMD
    FROM DOCTOR
    WHERE MCDP_CD in ('CS','GS')
    ORDER BY HIRE_YMD DESC, DR_NAME
```

### 평균 일일 대여 요금 구하기
```sql
    SELECT ROUND(AVG(DAILY_FEE),0) AS AVERAGE_FEE --ROUND(data, 자리수), AVG(평균낼 데이터)
    FROM CAR_RENTAL_COMPANY_CAR
    WHERE CAR_TYPE='SUV';
```

### 인기있는 아이스크림
```sql
    SELECT FLAVOR FROM FIRST_HALF
    ORDER BY TOTAL_ORDER DESC, SHIPMENT_ID ASC
```

### 서울에 위치한 식당 목록 출력하기
```sql
    SELECT A.REST_ID, B.REST_NAME, B.FOOD_TYPE, B.FAVORITES, B.ADDRESS, ROUND(AVG(A.REVIEW_SCORE),2) AS SCORE   -- AVG()를 기준으로 A>REVIEW_SCORE의 평균을 구하고, ROUND()를 이용하여 2+1번째 자리에서 반올림
    FROM REST_REVIEW A  -- REST_REVIEW를 기준으로 JOIN 연산을 수행, A라는 별칭을 줌
    INNER JOIN REST_INFO B ON A.REST_ID=B.REST_ID   -- ON으로 REST_ID를 조건으로 줌, REST_INFO의 별칭을 B로 함
    GROUP BY A.REST_ID  -- REST_ID로 그룹화
    HAVING B.ADDRESS LIKE '서울%'   -- 서울로 시작하는 주소를 가져옴
    ORDER BY SCORE DESC, B.FAVORITES DESC;  -- 각각을 조건에 맞게 정렬
```

### 조건에 부합하는 중고거래 댓글 조회하기
