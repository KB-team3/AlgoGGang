from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    for key, value in counter.items():
    
        # print(key, value)
        if value >= 2:
            answer += (value * (value-1) // 2) # nC2
    
    weights = set(weights)
    
    for w in weights:
        if w * 2/3 in weights:
            answer += counter[w*2/3] * counter[w]
        if w * 2/4 in weights:
            answer += counter[w*2/4] * counter[w]
        if w * 3/4 in weights:
            answer += counter[w*3/4] * counter[w]

    return answer