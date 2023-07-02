from collections import deque


def find(start, end, maps):
    # 맵의 크기를 저장
    w = len(maps[0])
    h = len(maps)
    visited = [[False] * w for _ in range(h)]
    queue = deque()
    check = False

    # BFS 시작하기 전 처음 값 찾기
    for i in range(h):
        for j in range(w):
            if maps[i][j] == start:
                queue.append((i, j, 0))
                visited[i][j] = True
                check = True
                break
        if check:
            break

    # 상, 우, 하, 좌
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while queue:
        y, x, time = queue.popleft()

        if maps[y][x] == end:
            return time

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h and maps[ny][nx] != "X":
                if not visited[ny][nx]:
                    queue.append((ny, nx, time + 1))
                    visited[ny][nx] = True

    return -1


def solution(maps):
    # 시작지점에서 레버까지
    p1 = find("S", "L", maps)
    # 레버에서 출구까지
    p2 = find("L", "E", maps)

    if p1 != -1 and p2 != -1:
        return p1 + p2
    else:
        return -1
