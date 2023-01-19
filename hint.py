def calcul_score(score):
    total = 0
    cnt=0
    for cost in score.values():
        total += cost
        cnt+=1
    print(total)
    return total/cnt

def max_min(score):
    score_lst = list(score.values())
    for i in range(len(score_lst)):
        for j in range(i,len(score_lst)):
            if score_lst[i] > score_lst[j]:
                score_lst[i],score_lst[j] = score_lst[j],score_lst[i]
    return (score_lst[-1],score_lst[0])

if __name__ == '__main__':
    score = {
        '최민호' : 210,
        '금나와라이' : 350,
        '자룡왕' : 650,
        '허수아비' : 290,
        '온유' : 180, 
    }
    
    print(calcul_score(score))
    print(max_min(score))
    for i in score.items():
        if i[1]==max_min(score)[1]:
            print(len(i[0]))

    

    
    # 점수들의 합 출력 하시오       답: 1680
    # 점수들의 평균을 출력 하시오   답: 336 또는 336.0
    # 가장 큰 점수와 작은 점수 출력하기 (튜플로 반환하시오)     답: (650,180)
    # 가장 낮은 점수를 갖은 사람의 이름은 몇글자 일까요?    답:2