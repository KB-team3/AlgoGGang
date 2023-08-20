from collections import defaultdict

def solution(weights):
    answer = 0
    dic = defaultdict(int)
    
    for w in weights:
        dic[w] += 1
        
    for d in dic:
        if dic[d] >= 2:
            answer += (dic[d] * (dic[d] - 1) // 2) 

    for w in set(weights):
        for v in (2/3, 2/4, 3/4):
            if w * v in weights:
                answer += dic[w*v] * dic[w]
            
    return answer
