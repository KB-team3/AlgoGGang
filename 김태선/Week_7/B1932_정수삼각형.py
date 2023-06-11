from sys import stdin

read = stdin.readline

lst = []
N = int(read())

for _ in range(N):
    lst.append(list(map(int, read().split())))

#list안에 리스트들을 하나씩 꺼내는데 2번째 리스트부터 꺼내기 때문에 range를 1부터 설정
for i in range(1, N):
    for j in range(len(lst[i])):
        
        #경우의 수 3가지 존재
        #제일 첫번째에 있는 경우, 즉 index가 항상 0인 애들
        if j == 0:
            lst[i][j] += lst[i-1][j]
        
        #제일 마지막에 있는 경우, 즉 리스트의 마지막 숫자들
        elif j == len(lst[i]) - 1:
            lst[i][j] += lst[i-1][j-1]
        
        #중간에 있는 애들 두가지 index 중에 가장 큰 값을 선정
        else:
            lst[i][j] += max(lst[i-1][j-1], lst[i-1][j])

print(max(lst[N-1]))