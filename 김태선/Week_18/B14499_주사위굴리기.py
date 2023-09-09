from sys import stdin
input = stdin.readline

n, m, x, y, k = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0 ,-1]

dice = [0 for _ in range(7)]
maps = [list(map(int, input().split())) for _ in range(n)]
order = list(map(int, input().split()))

def move(direction) : 
    # 동쪽
    if direction == 1 : 
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    # 서쪽
    elif direction == 2 : 
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    # 북쪽
    elif direction == 3 : 
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    # 남쪽
    elif direction == 4 : 
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

for i in order : 
    nx = x + dx[i - 1]
    ny = y + dy[i - 1]

    if nx < 0 or nx >= n or ny < 0 or ny >= m : 
        continue

    x, y = nx, ny
    move(i)

    if maps[x][y] : 
        dice[6] = maps[x][y]
        maps[x][y] = 0
    else : 
        maps[x][y] = dice[6]

    print(dice[1])
