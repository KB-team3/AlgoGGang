def solution(survey, choices):
    answer = ''
    score = dict()
    a0=['RT','TR']
    a1=['CF','FC']
    a2=['JM','MJ']
    a3=['AN','NA']
    arr=[a0,a1,a2,a3]
    for i,sur in enumerate(survey):
        for ar in arr:
            if sur in ar:
                sc=choices[i]-4
                if sur[0] not in score:
                    score[sur[0]]=0
                if sur[1] not in score:
                    score[sur[1]]=0    
                if sc>=0:
                    score[sur[0]]-=sc
                else:
                    score[sur[1]]+=sc
    for ar in arr:
        if ar[0][0] not in score:
            score[ar[0][0]]=0
            score[ar[0][1]]=0
        if score[ar[0][0]]>=score[ar[0][1]]:
            answer+=ar[0][0]
        else:
            answer+=ar[0][1]
    return answer

solution(["AN", "CF", "MJ", "RT", "NA"]	,[5, 3, 2, 7, 5]	)