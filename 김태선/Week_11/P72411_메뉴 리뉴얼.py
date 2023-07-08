from collections import Counter
from itertools import combinations


def solution(orders, course) : 
    answer = []

    for c_length in course : 
        temp = []

        for order in orders : 
            # 조합 라이브러리 함수(문자열 조합을 갯수에 맞게 계산)
            combi = combinations(sorted(order), c_length)
            # 문자열 조합을 temp에 저장
            temp += list(combi)

        # 계산 라이브러리 함수(딕셔너리 형태로 분류해서 총 가짓수를 구해줌)
        counter = Counter(temp)

        # 길이가 0 이상이고 가장 큰 조합 갯수가 최소 2번 이상인 값만 구해줌
        if len(counter) != 0 and max(counter.values()) != 1 :
            for c_factor in counter : 
                if counter[c_factor] == max(counter.values()) :
                    answer.append(''.join(c_factor)) # join 써서 문자열로 변환

    return sorted(answer)