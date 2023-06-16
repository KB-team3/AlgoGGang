import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

width, height = map(int, input().split())
N = int(input()) # 상점개수

ary = []
for _ in range(N):
    x, y = map(int, input().split())
    ary.append((x,y))

# 동근이 위치
X, Y = map(int, input().split())

totalDistance = 2 * (width + height)
answer = 0

for store in ary:
    # distance는 동근이의 거리임( (0,0) 기준으로 반시계했을 때 )
    if X == 1: # 북쪽
        distance = height + width + height + (width - Y)
    elif X == 2: # 남쪽
        distance = height + Y
    elif X == 3: # 서쪽
        distance = Y
    else: # 동쪽
        distance = height + width + (height - Y)
    
    # 상점의 위치를 구하기 (반시계)
    if store[0] == 1:
        distanceStore = height+width+height+( width - store[1])
    elif store[0] == 2:
        distanceStore = height + store[1]
    elif store[0] == 3:
        distanceStore = store[1]
    else:
        distanceStore = height + width + (height - store[1])
    
    d = abs(distance - distanceStore) # 반시계 거리
    
    d = min(d, totalDistance-d) # 반시계 vs 시계
    
    answer += d

print(answer)