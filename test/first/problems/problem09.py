# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
# 반드시 재귀함수로 구현해야 합니다.
def dec_to_bin(number):
    binary=''
    if number == 0 or number==1:    # number 가 0 또는 1일 때 리턴
        binary+=str(number)
        return binary
    elif number%2==1:               # 나머지가 1일 때 앞에 1 추가
        binary+='1'
        return dec_to_bin(number//2)+binary
    else:                           # 나머지가 0일 때 앞에 0 추가
        binary+='0'
        return dec_to_bin(number//2)+binary
    
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(dec_to_bin(10))  # 1010
    print(dec_to_bin(5))   # 101
    print(dec_to_bin(50))  # 110010
