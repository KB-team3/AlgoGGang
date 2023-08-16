def rank(num) : 
    if num > 1:
        return 6 - num + 1
    else :
        return 6
        
def solution(lottos, win_nums):
    answer = []
    
    zero = 0
    win = 0
    
    for num in lottos :
        
        if num == 0 :
            zero += 1
        else : 
            if num in win_nums :
                win += 1
    
    answer.append(rank(win+zero))
    answer.append(rank(win))
    
    return answer