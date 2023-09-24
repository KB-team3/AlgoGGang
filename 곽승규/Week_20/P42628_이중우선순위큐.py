import heapq

def solution(operations):
    answer = []
    h = [] # heap
    
    for o in operations:
        question = o.split(" ")
        if question[0] == "I":
            heapq.heappush(h, int(question[1]))
        elif question[0] == "D":
            if len(h) == 0:
                continue
            if question[1] == "1": # 큐에서 최대값 삭제
                tmp = []
                while len(h) != 0: # h에 -1을 모두 곱하여 최대값을 최소값으로 바꾸기
                    a = heapq.heappop(h)
                    a = a * -1
                    heapq.heappush(tmp, a)
                h = tmp.copy()
                heapq.heappop(h)
                # 다시 되돌리기
                tmp = []
                while len(h) != 0:
                    a = heapq.heappop(h)
                    a = a * -1
                    heapq.heappush(tmp, a)
                h = tmp.copy()
            else: # 큐에서 최소값 삭제
                heapq.heappop(h)
    if len(h) == 0:
        return [0,0]
    return [max(h), h[0]]