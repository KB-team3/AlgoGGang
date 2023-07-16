from heapq import heappop, heappush


def solution(book_time):
    answer = 1
    
    # "HH:MM" → HH * 60 + MM
    book_time_ref = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])) for s, e in book_time]
    book_time_ref.sort()
    
    heap = []
    for s, e in book_time_ref:
        if not heap:
            heappush(heap,e)
            continue
        if heap[0] <= s:
            heappop(heap)
        else:
            answer += 1
        heappush(heap,e+10)
    
    return answer