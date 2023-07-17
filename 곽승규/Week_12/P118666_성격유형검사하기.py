def solution(survey, choices):
    answer = ""
    # 지표 정보 리스트 생성
    zifo = [{"R": 0, "T": 0}, {"C": 0, "F": 0}, {"J": 0, "M": 0}, {"A": 0, "N": 0}]

    for s, num in zip(survey, choices):
        tmp = list(s)
        disagree = tmp[0]
        agree = tmp[1]

        # 현재 어떤 지표에 해당하는 건지 찾기
        index = 0
        for idx, z in enumerate(zifo):
            if disagree in z.keys():
                index = idx
                break

        if num == 1:  # 매우 비동의
            zifo[index][disagree] += 3
        elif num == 2:  # 비동의
            zifo[index][disagree] += 2
        elif num == 3:  # 약간비동의
            zifo[index][disagree] += 1
        elif num == 5:  # 약간동의
            zifo[index][agree] += 1
        elif num == 6:  # 동의
            zifo[index][agree] += 2
        elif num == 7:  # 매우동의
            zifo[index][agree] += 3

    # 정하기
    for dic in zifo:
        # zifo 값 순서대로 정렬
        sortedZifo = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        # 각 지표에서 값이 큰 거 찾기
        max_key = sortedZifo[0][0]
        answer += max_key

    return answer
