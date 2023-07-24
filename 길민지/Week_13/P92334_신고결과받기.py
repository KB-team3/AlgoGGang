def solution(id_list, report, k):
    # 신고 당한 횟수 딕셔너리 초기화
    count = dict.fromkeys(id_list, 0)

    # 신고 기록 딕셔너리 생성 및 카운트
    reportDict = {}
    for i in id_list:
        reportDict[i] = []
    for r in report:
        reportId = r.split(" ")
        if reportId[1] in reportDict[reportId[0]]:
            continue
        reportDict[reportId[0]].append(reportId[1])
        count[reportId[1]] += 1
    answer = [0] * len(id_list)

    # 메일 보낼 사람 확인
    for reported in count:
        if k <= count[reported] :
            for i in range(len(id_list)):
                if reported in reportDict[id_list[i]]:
                    answer[i] += 1
    return answer