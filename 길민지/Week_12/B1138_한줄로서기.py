N = int(input())
input = list(map(int, input().split()))

answer = [0] * N
for i in range(N):
  # 빈 칸이 input[i]개 되는 자리에 넣기
  cnt = 0
  for j in range(N):
    if answer[j]!=0:
      continue
    if cnt == input[i]:
      answer[j]=i+1
      break
    cnt+=1
print(*answer)