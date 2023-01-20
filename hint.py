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
    for item in score.items():          # 나는 제일 작은놈의 이름을 일단 가져올거야 그럼 저 딕셔너리의 item이 필요하겠지
        if item[1]==max_min(score)[1]:  # item에 두번째놈(item[1])이 점수야 이게 젤 낮은 놈(max_min(score)[1])을 찾겠다.
            print(len(item[0]))         # 그자식의 이름(item[0])을 꺼내와서 길이(len)를 재자

    
    # 점수들의 합 출력 하시오       답: 1680
    # 점수들의 평균을 출력 하시오   답: 336 또는 336.0
    # 가장 큰 점수와 작은 점수 출력하기 (튜플로 반환하시오)     답: (650,180)
    # 가장 낮은 점수를 갖은 사람의 이름은 몇글자 일까요?    답:2
    # hint