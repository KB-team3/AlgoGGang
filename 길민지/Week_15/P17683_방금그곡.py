def change(text):
    text = text.replace("C#", "H")
    text = text.replace("D#", "I")
    text = text.replace("F#", "J")
    text = text.replace("G#", "K")
    text = text.replace("A#", "L")
    return text

def solution(m, musicinfos):
    answer = '(None)'
    m = change(m) # 멜로디 치환
    
    list = []
    for musicinfo in musicinfos:
        info = musicinfo.split(',')
        
        # 시간 계산
        t1 = info[0].split(':')
        t2 = info[1].split(':')
        time = (int(t2[0]) - int(t1[0])) * 60 + int(t2[1]) - int(t1[1])
        
        # 악보 치환 및 시간에 맞게 변경
        music = change(info[3])
        music = music * (time // len(info[3]) + 1)
        title = info[2]
        list.append([time, title, music[0:time]])
    
    t = 0
    for music in list:
        if(m in music[2] and t < music[0]):
            t = music[0]
            answer = music[1]
        
    return answer