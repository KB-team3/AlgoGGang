from sys import stdin
input = stdin.readline

# 왼쪽 위 모서리를 기준으로 0을 잡고 일자로 펼쳤을 때 얼마나 떨어졌는지 위치를 계산
def dist(x, y) : 
    if x == 1 : # 북쪽
        return y
    if x == 2 : # 남쪽
        return w + h + w - y
    if x == 3 : # 서쪽
        return w + h + w + h - y
    if x == 4 : # 동쪽
        return w + y
    
w, h = map(int, input().split()) # 총 가로세로 길이
n = int(input()) # 상점 갯수

direction = []

for _ in range(n + 1) : # 일자로 펼쳤을 때 0에서 상점까지 거리
    x, y = map(int, input().split())
    direction.append(dist(x, y))

ans = 0

for i in range(n) : # 동근이와 상점 사이 최단거리 계산
    in_direction = abs(direction[-1] - direction[i]) # 한 방향으로 거리 구할 때 거리의 차
    out_direction = (w + h + w + h) - in_direction # 그 반대 방향ㅇ으로 거리 구할 때 거리 차
    ans += min(in_direction, out_direction) # 두 개중 작은 값 더함

print(ans)
