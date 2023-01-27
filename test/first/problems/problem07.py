# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def calculator(*numbers):
    if len(numbers) == 1:                       # pi는 3.14로 계산
        return (numbers[0]**2)*3.14
    elif len(numbers)==2:
        if sum(numbers)%2!=0:                   # 짝수 홀수 검사
            return (numbers[0]*numbers[1])/2    # 삼각형 넓이(밑변*높이/2)
        else:
            return numbers[0]*numbers[1]        # 사각형 넓이(밑변*높이)
    elif len(numbers)>=3:                       # 3개 이상일 때
        return (sum(numbers), sum(numbers)/len(numbers))
    else:
        return 0
    
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(calculator(5))                # 78.5
    print(calculator(10, 20))           # 200
    print(calculator(10, 20, 30, 40))   # (100, 25.0)
    print(calculator())                 # 0