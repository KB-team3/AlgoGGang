import heapq

def solution(operations):
    answer = []
    heap = []
    
    for o in operations:
        lst = o.split(" ")
        if lst[0] == 'I':
            heapq.heappush(heap, int(lst[1]))
        elif len(heap) > 0 and lst[1] == '-1':
            heapq.heappop(heap)
        elif len(heap) > 0 and lst[1] == '1':
            heap2 = []
            for h in heap:
                heapq.heappush(heap2, (-int(h), int(h)))
            heapq.heappop(heap2)
            heap = []
            for h in heap2:
                heapq.heappush(heap, h[1])
    
    if len(heap) == 0:
        return [0, 0]
    else:
        return [max(heap), min(heap)]
