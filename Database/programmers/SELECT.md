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

