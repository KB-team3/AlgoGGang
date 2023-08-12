def solution(lottos, win_nums):
    zero = lottos.count(0) # 0의 개수
    
    set_lottos = set(lottos)
    set_wins = set(win_nums)
    if(0 in set_lottos) :
        set_lottos.remove(0)
    diff = set_lottos - set_wins
    correct = 6 - zero - len(diff) # 맞은 번호 개수
    
    # 최저 순위
    worst = 6 if (correct == 0)  else 7 - correct
    
    # 최고 순위
    correct += zero # 0까지 다 맞은 경우
    best = 6 if (correct == 0) else 7 - correct
    return [best, worst]