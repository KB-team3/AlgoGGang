def solution(id_list, report, k):
    report = set(report) # 중복을 제거
    answer = {x:0 for x in id_list} # 메일을 보낼 횟수
    reports = {x:0 for x in id_list} # 각 신고 당한 횟수
    
    for r in report:
        reports[r.split()[1]] += 1 # 빈칸을 기준으로 인덱스 1번의 친구가 신고를 당했으므로 += 1 해줌
    
    for r in report: # 신고당한 횟수 > k 이면 메일 보내기
        a = r.split()[0] # 신고한 사람
        b = r.split()[1] # 신고당한 사람
        if reports[b] >= k:
            answer[a] += 1 # 메일 횟수 += 1해줌
    
    return list(answer.values())