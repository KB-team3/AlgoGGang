from sys import stdin 
input = stdin.readline

r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]
front = 0
back = 0  

# 공기청정기 위치 설정
for i in range(r) : 
    if room[i][0] == -1 : 
        front = i
        back = i + 1
        break

# 미세먼지 이동
def dust() : 
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    temp = [[0] * c for _ in range(r)]

    for i in range(r) : 
        for j in range(c) : 
            if room[i][j] != 0 and room[i][j] != -1 : 
                value = 0
                for k in range(4) : 
                    nx = i + dx[k]
                    ny = j + dy[k]

                    # 이동한 좌표가 방 안에 있거나 공기청정기 자리가 아닌 경우
                    if 0 <= nx < r and 0 <= ny < c and room[nx][ny] != -1 : 
                        temp[nx][ny] += room[i][j] // 5
                        value += room[i][j] // 5
                
                room[i][j] -= value
   
    # 미세먼지 설정완료
    for i in range(r) : 
        for j in range(c) : 
            room[i][j] += temp[i][j]

# 공기청정기 위쪽 이동
def air_up() : 
    # 반시계 방향(동북서남)
    dx = [0,-1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0  # 현재 위치의 미세먼지 값
    x, y = front, 1     # 시작 지점 설정

    while True : 
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == front and y == 0 : 
            break
        if not 0 <= nx < r or not 0 <= ny < c : 
            direct += 1
            continue
        room[x][y], before = before, room[x][y]
        x, y = nx, ny

# 공기청정기 아래쪽 이동
def air_down() : 
    # 시계 방향(동남서북)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = back, 1

    while True : 
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == back and y == 0 : 
            break
        if not 0 <= nx < r or not 0 <= ny < c : 
            direct += 1
            continue
        room[x][y], before = before, room[x][y]
        x, y = nx, ny

# t초 동안 실행
for _ in range(t) : 
    dust()
    air_up()
    air_down()

# 결과값 출력
res = 0
for i in range(r) : 
    for j in range(c) : 
        if room[i][j] > 0 : 
            res += room[i][j]

print(res)
