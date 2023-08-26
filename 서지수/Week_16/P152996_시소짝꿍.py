import math
from collections import Counter


def solution(weights):
    answer = 0
    counter = Counter(weights)
    for w in weights:
        counter[w] -= 1
        if w in counter:
            answer += counter[w]
        if 2 * w in counter:
            answer += counter[2*w]
        if 3/2 * w in counter:
            answer += counter[(3/2)*w]
        if 2/3 * w in counter:
            answer += counter[(2/3)*w]
        if 4/3 * w in counter:
            answer += counter[(4/3)*w]
        if 3/4 * w in counter:
            answer += counter[(3/4)*w]
        if 2/4 * w in counter:
            answer += counter[(2/4)*w]
        counter[w] += 1
    return answer//2