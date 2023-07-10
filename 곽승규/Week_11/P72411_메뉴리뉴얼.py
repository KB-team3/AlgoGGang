from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []

    for c in course:
        temp = []
        for order in orders:
            combination = combinations(sorted(order), c)  # 정렬해서 조합 생성
            combination_list = list(combination)  # 조합을 리스트로 변환
            temp += combination_list  # 하나의 리스트에 다 저장

        counter = Counter(temp)  # Counter(temp)를 하면 위의 조합별로 횟수를 계산

        if len(counter) != 0 and max(counter.values()) != 1:
            for i in counter:
                if counter[i] == max(counter.values()):
                    answer += ["".join(i)]
    return sorted(answer)
