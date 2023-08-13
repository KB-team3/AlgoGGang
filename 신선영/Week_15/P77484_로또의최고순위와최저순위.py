def solution(lottos, win_nums):
    zero = 0    # 알아볼 수 없는 번호의 수
    yes = 0     # 당첨된 번호의 수

    for l in lottos:
        if l == 0:
            zero += 1
        elif l in win_nums:
            yes += 1
    
    a = 7 - (yes + zero)    # 알아볼 수 없는 것도 모두 일치한다고 가정
    b = 7 - yes
    if a >= 7:  # 한개도 안 맞는 경우 낙첨이니 6등으로 변환
        a = 6
    if b >= 7:
        b = 6
    
    return [a, b]
