# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    dy = [-1,1,0,0] # 상 하 좌 우
    dx = [0,0,1,-1]
    
    # 좌표값이 0보다 작아지거나 최대값(N)을 벗어나는 경우 False를 반환
    if position[0]+dy[M]<0 or position[1]+dx[M]<0 or position[0]+dy[M]>N or position[0]+dx[M]>N:
        return False
    else:   # 그 외에는 이동 할 수 있는 좌표이므로 True를 반환
        return True
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
