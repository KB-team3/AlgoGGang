from queue import PriorityQueue


def solution(book_time):
    # 분으로 바꿔서 다시 담을 리스트
    book = []

    for time in book_time:
        startHour, startMinute = map(int, time[0].split(":"))
        endHour, endMinute = map(int, time[1].split(":"))

        # 모두 분으로 바꾸기
        tmpStart = startHour * 60 + startMinute
        tmpEnd = endHour * 60 + endMinute
        book.append([tmpStart, tmpEnd])

    # 입실 시간을 기준으로 정렬
    book.sort(key=lambda x: x[0])

    # 방이 몇 개 필요한지 체크
    count = 1  # 최소 한개는 필요 함
    outTimeQueue = PriorityQueue()  # 우선순위 큐 생성
    outTimeQueue.put(book[0][1] + 10)  # 첫번째 퇴실 시간 + 청소시간

    for time in book[1:]:  # 두번째 시간부터 봄
        inTime = time[0]
        outTime = outTimeQueue.get()

        if outTime > inTime:  # 퇴실시간 + 10(청소시간) vs 다음 입실시간
            count += 1
            outTimeQueue.put(outTime)  # 다시 우선순위 큐에 넣기
            outTimeQueue.put(time[1] + 10)  # 추가된 방의 퇴실 시간 큐에 넣기
        else:
            outTimeQueue.put(time[1] + 10)

    return count
