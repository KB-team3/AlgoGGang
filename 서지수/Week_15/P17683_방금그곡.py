def solution(m, musicinfos):
    for i in range(len(musicinfos)):
        time_1 = int(musicinfos[i].split(",")[1].split(":")[0])*60+int(musicinfos[i].split(",")[1].split(":")[1])
        time_2 = int(musicinfos[i].split(",")[0].split(":")[0])*60+int(musicinfos[0].split(",")[1].split(":")[1])

        if len(m)<time_1-time_2:
            melody=musicinfos[i].split(",")[3]
            count=0
            for j in range(len(m)):
                for k in range(len(melody)):
                    if j+1<len(m) and m[j+1]=="#":
                        if k+1<len(melody) and m[j]==melody[k] and melody[k]=="#":
                            count+=1
                    else:
                       if m[j]==melody[k]:
                            count+=1
            if count==len(m):
                return musicinfos[i].split(",")[2]   
        
        
print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
