# 재귀 깊이 제한 변경
import sys
limit_number = 10000
sys.setrecursionlimit(limit_number)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def DFS(maps, x, y):
    days = int(maps[x][y])
    isChecked[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(nx<0 or ny<0 or len(maps)<=nx or len(maps[0])<=ny): continue
        if maps[nx][ny] == 'X' or isChecked[nx][ny] == 1: continue
        days += DFS(maps, nx, ny)
    return days

def solution(maps):
    answer = []
    global isChecked
    isChecked = [[0]*len(maps[0]) for _ in range(len(maps))]
    
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] == 'X' or isChecked[i][j] == 1:
                continue
            days = DFS(maps, i, j)
            answer.append(days)
    
    if len(answer)==0:
        answer.append(-1)
    answer.sort()
    return answer