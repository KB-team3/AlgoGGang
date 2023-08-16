def solution(lottos, win_nums) : 

    # 리스트 요소 중 count로 원하는 요소 세기
    cnt_zero = lottos.count(0) 
    cnt_win = 0     # 맞춘 개수(초기화 0 설정)
    # 맞춘 개수에 따른 순위 할당
    scores = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

    for i in lottos : 
        if i in win_nums : 
            cnt_win += 1

    highest = cnt_win + cnt_zero    # 0이 다 맞았을 경우
    lowest = cnt_win # 0이 다 틀렸을 경우

    # 딕셔너리 key로 순위 계산
    return [scores[highest], scores[lowest]]