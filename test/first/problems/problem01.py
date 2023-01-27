# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def average(scores):
    total = 0
    cnt = 0                     # 점수의 개수
    for score in scores:        # 전체 점수 합산 sum을 사용하지 않고 구현
        total += score  
        cnt += 1
    return total/cnt  # 평균을 출력(반올림 관련 조건 X)
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(average(scores))    # 82.5