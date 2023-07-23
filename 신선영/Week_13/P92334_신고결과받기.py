def solution(id_list, report, k):
    answer = [0] * len(id_list)  # id들이 신고당한 횟수만 기록할것임
    report = set(report)  # 동일한 유저 신고 횟수는 1회로 처리 - 중복 제거
    for r in report:
        a, b = r.split(' ')
        for i in range(len(id_list)):
            if id_list[i] == b:  # 신고당한 유저 횟수 1 더함
                answer[i] += 1
    return answer
