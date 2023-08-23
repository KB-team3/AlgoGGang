from collections import Counter
import math 
def solution(weights):
    answer = 0
    seesaws = [2, 3/2, 4/3]
    
    # 배수 몸무게 세기
    for weight in weights:
        for seesaw in seesaws:
            if (weight*seesaw in weights):
                answer+=1
                
    # 같은 몸무게 세기
    same = dict(Counter(weights))
    for s in same:
        if same[s]>1:
            answer += math.comb(same[s], 2)
            
    return answer