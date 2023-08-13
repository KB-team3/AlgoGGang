def getNotes(lst, length):  # 텍스트로 주어진 음을 리스트로 바꿈 (# 포함)
    notes = []
    for i in range(length):
            if lst[i] == "#":
                notes.pop(-1)
                notes.append(lst[i - 1:i + 1])
            else:
                notes.append(lst[i])
    return notes

def solution(m, musicinfos):
    answer = ["(None)", 0] # 일치하는 값 없는 경우 (None) 출력
    m = getNotes(m, len(m))
    
    for i in musicinfos:
        info = i.split(",")
        
        # 음악 재생 가능한 시간 (초 단위로 계산)
        sec = (int(info[1].split(":")[0]) - int(info[0].split(":")[0])) * 60 + int(info[1].split(":")[1]) - int(info[0].split(":")[1])
        
        notes = getNotes(info[3], len(info[3]))
        
        # 제시된 음악의 음을 초만큼 계산
        fullnotes = notes * (sec // len(notes)) + notes[:sec % len(notes)]
        for i in range(len(fullnotes) - len(m) + 1):
            # 포함되는 경우 찾기
            if fullnotes[i : i + len(m)] == m:
                if sec > answer[1]:
                    answer[0] = info[2]
                    answer[1] = sec
            
    return answer[0]
