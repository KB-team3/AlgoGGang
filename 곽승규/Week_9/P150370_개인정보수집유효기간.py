def solution(today, terms, privacies):
    answer = []

    # 오늘 날짜정보를 일로 변경
    tmp = today.split(".")
    sumDay = (int(tmp[0]) * 28 * 12) + (int(tmp[1]) * 28) + int(tmp[2])

    # 약관 종류 딕셔너리 저장
    term = {}
    for i in terms:
        temp = i.split()
        term[temp[0]] = temp[1]

    cnt = 1
    for i in privacies:
        date, type = i.split()
        tmp = date.split(".")
        # 날짜정보를 일로 변경
        sumD = (int(tmp[0]) * 28 * 12) + (int(tmp[1]) * 28) + int(tmp[2])
        # 비교하기
        if (int(term[type]) * 28) <= abs(sumD - sumDay):
            answer.append(cnt)
        cnt += 1

    return answer
