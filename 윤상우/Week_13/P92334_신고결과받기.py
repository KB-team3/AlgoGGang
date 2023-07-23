def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_dict = {}
    idx_dict = {}
    
    report = list(set(report)) 
    for i in range(len(id_list)):
        report_dict[id_list[i]] = []
        idx_dict[id_list[i]] = i

    for i in report:
        report_dict[i.split(' ')[1]].append(i.split(' ')[0]) 
    for value in report_dict.values():
        if len(value) >= k:
            for j in value:
                answer[idx_dict[j]] += 1
                                
    return answer