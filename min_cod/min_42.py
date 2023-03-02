"""
# 김밥 속재료

s=input()

def abc(level=3,idx=0,ss=''):
    if level==0:
        print(ss)
        return
    for i in range(len(s)):
        if i>=idx:
            abc(level-1,i,ss+s[i])

abc()
"""

# best Number 선정하기

calc=[0]*5

numbers= list(map(int,input().split()))

Min = 28e8
Max = -28e8



