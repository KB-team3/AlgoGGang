def solution(numbers, target) : 
    ans = 0

    # dfs 재귀함수 사용
    def dfs(num, index) :   #현재까지의 합 : num, 탐색 중인 현재의 숫자 인덱스 : index
        # 외부 변수 함수 내에서 사용
        nonlocal ans
        # 현재 인덱스가 마지막 인덱스인 경우
        if index == len(numbers) : 
            if num == target : 
                ans += 1
            return 0
        else :  # 숫자를 더하거나 뺄 수 있는 경우
            dfs(num + numbers[index], index + 1)
            dfs(num - numbers[index], index + 1)

    # 초기값 설정
    dfs(0, 0)
    
    return ans
    