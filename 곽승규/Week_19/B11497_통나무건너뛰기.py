import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())

for t in range(T):
  N = int(input())
  ary = list(map(int, input().split()))
  ary = sorted(ary) # 우선 오름차순 정렬
  answer = 0
  
  for j in range(2, N):
    answer = max(answer, ary[j] - ary[j-2])
    
  print(answer)
    
  
  