def solution(book_time):
    answer = []
    # 끝나는 시간을 기준으로 정렬
    book_time.sort(key = lambda x : x[1], reverse=True)
    
    for book in book_time:
        con = False
        for ans in answer:
            a = int(ans[-1][0].split(":")[0]) * 60 + int(ans[-1][0].split(":")[1])
            b = int(book[1].split(":")[0]) * 60 + int(book[1].split(":")[1]) + 10  # 10분 청소시간
            if a >= b:
                # 가능한 경우 연결
                ans.append(book)
                con = True
                break
        # 가능한 경우가 없었던 경우 새 리스트 생성
        if con == False:
            answer.append([book])

    return len(answer)
