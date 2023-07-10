from collections import defaultdict
N = int(input())


def solution(N):
    def visited(origin, added):
        return origin | (1 << added)

    dp = [[defaultdict(int) for _ in range(N)] for _ in range(10)]
    for i in range(1, 10):
        dp[i][0] = {visited(0, i): 1}
    for j in range(1,N):
        for i in range(10):
            if i-1 != -1:
                for k, v in dp[i-1][j-1].items():
                    new_visited = visited(k, i)
                    dp[i][j][new_visited] += v
            if i+1 != 10:
                for k, v in dp[i+1][j-1].items():
                    new_visited = visited(k, i)
                    dp[i][j][new_visited] += v
    answer = 0
    for i in range(10):
        for k, v in dp[i][N-1].items():
            if k == 1023:
                answer += v
    return answer%1000000000


print(solution(N))


