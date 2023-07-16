from sys import stdin
input = stdin.readline

n = int(input())
p = list(map(int, input().split()))
ans = [0] * n

for i in range(n) : 
    # 자신의 왼쪽에 키 큰 사람의 수
    cnt = 0

    for j in range(n) :
        # 자신의 왼쪽에 있는 키 큰 사람의 수와 맞고, 그 자리에 아무도 없는 경우
        if cnt == p[i] and ans[j] == 0 :
            # 현재 사람의 인덱스ㅇ의 값이므로 +1 
            ans[j] = i + 1
            break

        #자리에 아무도 없는 경우, 자신의 왼쪽에 키 큰 사람의 수를 카운트    
        elif ans[j] == 0 : 
            cnt += 1

# 언패킹을 통해 리스트 값 요소들 공백으로 구분하여 출력
print(*ans)