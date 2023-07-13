def solution(book_time):
    answer = 0
    con = [0 for _ in range(24*60+11)]
    for start, end in book_time:
        start = list(map(int, start.split(":")))
        start = start[0]*60+start[1]
        end = list(map(int, end.split(":")))
        end = end[0]*60+end[1]
        con[start]+=1
        con[end+10]-=1
    for i in range(24*60+10):
        con[i+1]+=con[i]
        answer = max(answer, con[i+1])
    return answer