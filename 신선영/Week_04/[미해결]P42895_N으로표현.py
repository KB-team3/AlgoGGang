def solution(N, number):
    answer = 0
    
    DP = [[], [N]]
    
    for i in range(1, 8):
        l = set()
        for d in DP[i]:
            l.add(d + N)
            l.add(d - N)
            l.add(d * N)
            l.add(N - d)
            l.add(d * N)
            l.add(d * 10 + N)
            if d != 0:
                l.add(N // d)
            if N != 0:
                l.add(d // N)
        if number in l:
            return i + 1
        DP.append(l)

    
    return -1