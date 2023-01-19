# # 데일리 실습 2-2

# st="<div>오늘은 기분이 좋아</div>"
# st=st[5:-6]
# print(st)

# st="<div>오늘은 기분이 좋아</div>"
# st=st[st.find('>')+1:st.find('<',1)]

# str_lst = input().lower().split()

# ret = ((str_lst[0][-1] == str_lst[1][0])and (str_lst[1][-1]==str_lst[-1][0]))

# if ret:
#     print('Pass')
# else:
#     print('Fail')

# name = 'kevin'
# height = 173
# weight = 64.321

# print(f'{name}의 키는 {height}cm이며 몸무게는 {weight}kg 입니다.')
# print(f'{name}의 키는 {height}cm이며 몸무게는 {weight:.1f}kg 입니다.')
# print(f'{name}의 키는 {height}cm이며 몸무게는 {weight:.2f}kg 입니다.')
# print(f'{name}의 키는 {height}cm이며 몸무게는 {weight:f}kg 입니다.')

# # 문자 정렬하기
# print(f'내 이름은 {name:>8} 입니다.')   # 8칸의 공간에 name을 넣겠다 + 우측정렬(>)
# print(f'내 이름은 {name:<8} 입니다.')   # 8칸의 공간에 name을 넣겠다 + 좌측정렬(<)
# print(f'내 이름은 {name:^8} 입니다.')   # 8칸의 공간에 name을 넣겠다 + 중앙정렬(^)
# print(f'내 이름은 {name:8} 입니다.')    # 8칸의 공간에 name을 넣겠다 + default(문자는 왼쪽 정렬)

# # 정수값 정렬하기
# print(f'키는{height:8}입니다')          # 부호가 없으면 오른쪽 정렬이 default(숫자는 오른쪽 정렬)
# print(f'키는{height:>8}입니다')
# print(f'키는{height:<8}입니다')
# print(f'키는{height:^8}입니다')

# print(f'키는{height:08}입니다')

# height=1000000
# print(f'키는{height:>10,}입니다')       # , 찍으면 금액 표기에 쓸 수 있음


# #출력 결과 예시
# # 스테이크   50,000
# # + VAT     7,500
# # 총계 ₩    57,500

# steak = 50000
# VAT = int(steak * 0.15)

# print(f'스테이크{steak:>8,}') #스테이크가격을 우측에 정렬 후 , 넣기 
# print(f'+ VAT{VAT:>10,}')
# print(f'총계 ₩{(steak+VAT):>10,}')

