from collections import defaultdict


def solution(weights):
    answer = 0

    weights_dict = defaultdict(float)
    ratio = [1/1, 1/2, 2/1, 2/3, 3/2, 3/4, 4/3]
    
    for w in weights:
        for r in ratio:
            # 몸무게와 비율을 곱한 모든 값을 저장
            answer += weights_dict[r * w]
        weights_dict[w] += 1

    return int(answer)