def trans_sharp(str):
    str = str.replace("A#", "a")
    str = str.replace("C#", "c")
    str = str.replace("D#", "d")
    str = str.replace("F#", "f")
    str = str.replace("G#", "g")
    return str

def solution(m, musicinfos):
    answer = ''
    res = []

    for info in musicinfos:
        info_bits = info.split(",")

        start_h, start_m = map(int, info_bits[0].split(":"))
        end_h, end_m = map(int, info_bits[1].split(":"))
        duration = (end_h - start_h) * 60 + (end_m - start_m)

        title = info_bits[2]
        melody = trans_sharp(info_bits[3])

        repeat = 60 // duration

        full = ""
        for cnt in range(repeat):
            full += melody

        if trans_sharp(m) in full:
            res.append(title)
        answer = " ".join(res)

    return answer