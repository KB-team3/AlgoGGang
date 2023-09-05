n = int(input())
array = [0]*10001

for i in range(1, n+1):
    array[i] = int(input())

M = [0]*10001
M[1] = array[1]
M[2] = array[1] + array[2]
M[3] = max(array[3] + array[1], array[3] + array[2], M[2])
for i in range(4, n+1):
    M[i] = max(array[i] + M[i-2], array[i] + array[i-1] + M[i-3], M[i-1])
# test 출력
# print("array", array)
print(max(M))