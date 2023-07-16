def solution(book_time):
    time = [0] * (24 * 60)

    # 분으로 전환
    book = []*len(book_time)
    for b in book_time:
        in_time = list(map(int, b[0].split(":")))
        out_time = list(map(int, b[1].split(":")))
        book.append([in_time[0] * 60 + in_time[1], out_time[0] * 60 + out_time[1] + 10])

    # 대실 중인 시간 기록
    for b in book :
        for i in range (b[0], b[1] if b[1]<1440 else 1440):
            time[i]+=1

    return max(time)
