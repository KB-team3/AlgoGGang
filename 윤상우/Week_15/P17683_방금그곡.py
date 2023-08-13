def change(n) : 
    return n.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')

def solution(m, musicinfos):
    m = change(m)
    answer = {'time' : 0, 'song' : '(None)'}
    
    for music in musicinfos :
        info = music.split(',')
        start_h, start_m = map(int,info[0].split(':'))
        end_h, end_m = map(int,info[1].split(':'))
        time = (end_h-start_h)*60 + end_m-start_m
        name = info[2]
        note = change(info[3])
        
        heard = ''
        
        for n in range(time) :
            heard += note[n%len(note)]
            
        if m in heard:
            if time > answer['time'] : 
                answer['time'] = time
                answer['song'] = name
        
    return answer['song']