import math


def solution(m, musicinfos) : 
    answer = None   # 변수 초기화
     # #부터 있는 글자를 한 글자로 취급하기 위해 치환
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#",
"g").replace("A#", "a")
    
    for musicinfo in musicinfos : 
        start, end, title, code = musicinfo.split(",")

        hour, minute = map(int, start.split(":"))
        start = hour * 60 + minute

        hour, minute = map(int, end.split(":"))
        end = hour * 60 + minute
        duration = end - start  # 곡의 재생시간

        code = code.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#",
"g").replace("A#", "a")
        # 음악이 반복되는 횟수 계산
        code *= math.ceil(duration / len(code))
        code = code[:duration]

        if m not in code : 
            continue
        
        # 이 부분이 이해 안감
        if answer == None or answer[0] < duration or (answer[0] == duration and
    answer[1] > start) : 
            answer = (duration, start, title)

    if answer : 
        # title 값 return
        return answer[-1]
    
    return "(None)"