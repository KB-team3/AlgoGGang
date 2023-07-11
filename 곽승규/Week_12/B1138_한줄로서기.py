import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())  # 사람 수
tallerThanMe = list(map(int, input().split()))  # 나보다 키가 큰 사람이 왼쪽에 몇 명

answer = [0] * N
visited = [False] * N
for i in range(N):
    count = 0
    tallNum = tallerThanMe[i]
    for j in range(N):
        if not visited[j]:  # 빈칸 있으면
            if count == tallNum:  # 빈칸 카운트한 값 == 내 앞에 키 큰사람 수
                visited[j] = True
                answer[j] = i + 1
                break
            count += 1

print(*answer)
