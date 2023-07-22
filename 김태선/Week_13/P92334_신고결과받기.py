def solution(id_list, report, k):
    # 모든 key(사용자의 ID)에 대해 0으로 초기화하는 딕셔너리
    notify_cnt = {i:0 for i in id_list}
    # list길이 만큼의 모든 리스트를 0으로 초기화
    mail_cnt = [0] * len(id_list)

    # 중복 제거를 위해 set 사용
    for r in set(report) : 
        # report = 사용자ID 신고한ID
        notify_cnt[r.split(" ")[1]] += 1

    for r in set(report) :
        if notify_cnt[r.split(" ")[1]] >= k :
            # 사용자ID가 저장된 index 값 반환
            mail_cnt[id_list.index(r.split(" ")[0])] += 1

    return mail_cnt