from sys import stdin
input = stdin.readline

N = int(input())
K = int(input())
sensor = list(map(int, input().split()))

# 센서 오름차순 정렬
sensor.sort()

# 센서 거리 차 계산
sensor_diff = [sensor[i] - sensor[i - 1] for i in range(1, N)]

# 거리 차들 오름차순 정렬
sensor_diff.sort()

print(sum(sensor_diff[:N - K]))
