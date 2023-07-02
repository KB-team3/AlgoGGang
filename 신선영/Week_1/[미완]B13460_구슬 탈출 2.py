# [BOJ] 13460. 구슬 탈출 2

import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 세로, 가로
board = [input().split() for _ in range(N)]
print(board)
