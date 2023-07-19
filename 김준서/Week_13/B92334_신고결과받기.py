from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    report_count = defaultdict(int)
    mail_sent=defaultdict(int)
    who_reported=defaultdict(set)
    for r in report:
        one, vic = list(r.split())
        if one not in who_reported[vic]:
            report_count[vic]+=1
            who_reported[vic].add(one)
    for key,value in report_count.items():
        if value>=k:
            for rep in who_reported[key]:
                mail_sent[rep]+=1
    for id in id_list:
        answer.append(mail_sent[id])
    return answer