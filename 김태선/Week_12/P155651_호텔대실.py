from collections import defaultdict


def solution(book_time):
    answer = 0
    
    # 시간 빠른 순으로 정렬
    book_time.sort()

    # defaultdict으로 기본값 0으로 저장 
    # db = 이용 종료시간 딕셔너리 
    db = defaultdict(int)

    for start, end in book_time : 
        start = start.split(":")
        end = end.split(":")
        start_time = int(start[0]) * 60 + int(start[1])
        end_time = int(end[0]) * 60 + int(end[1])

        # 퇴실 시간 확인
        # db 딕셔너리 키인 방 for문으로 순회
        for room in db.keys() : 
            if db[room] <= start_time : 
                db[room] = end_time + 10
                break
        # 적절한 방을 찾지 못했을 경우
        else : 
            db[answer] = end_time + 10
            # 방 하나 추가
            answer += 1

    return answer
