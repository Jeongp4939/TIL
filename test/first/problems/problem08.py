# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    new_word = ''
    for char in word:
        if char.isupper():  # 대소문자 확인, ascii 가 z를 벗어날 시 a부터 다시
            new_word += chr(ord(char)+n) if ord(char)+n<=90 else chr(ord(char)+n-26)
        else:               # 알파벳은 26개 이므로 -26
            new_word += chr(ord(char)+n) if ord(char)+n<=122 else chr(ord(char)+n-26)
    return new_word
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(caesar('apple', 5))      # fuuqj
    print(caesar('ssafy', 1))      # ttbgz
    print(caesar('Python', 10))    # Zidryx
