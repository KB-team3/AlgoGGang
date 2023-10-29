import sys

# 행 체크
def row(i, n, board):
  for x in range(9):
    if board[i][x] == n:
      return False
  return True

# 열 체크
def column(j, n, board):
  for x in range(9):
    if board[x][j] == n:
      return False
  return True

# 사각형 체크
def rect(i, j, n, board):
  for x in range(i//3*3, i//3*3+3):
    for y in range(j//3*3, j//3*3+3):
      if board[x][y] == n:
        return False
  return True

# 숫자 결정 함수
def solution(i, j, board):
  # 9x9 다 채웠으면 출력 후 종료
  if i>=9:
    for b in board:
      for x in b:
        print(x, end="")
      print('')
    exit(0)

  # 이미 채워진 칸이면 다음 칸으로
  if board[i][j]  != 0:
    solution(i+1, 0, board) if j>=8 else solution(i, j+1, board)
    return

  # 해당 칸에 들어갈 수 있는 숫자 넣고 다음 칸으로
  for n in range(1, 10):
    if row(i, n, board) and column(j, n, board) and rect(i, j, n, board):
      board[i][j] = n
      solution(i+1, 0, board) if j>=8 else solution(i, j+1, board)
      board[i][j] = 0

# 입력
board = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(9)]
# 숫자 채우기
solution(0, 0, board)