def solution(numbers, target):
    return dfs(numbers, target, 0, 0)
    
def dfs(numbers, target, idx, sum):
    if idx == len(numbers):
        return 1 if sum == target else 0

    ways = 0
    ways += dfs(numbers, target, idx + 1, sum + numbers[idx])
    ways += dfs(numbers, target, idx + 1, sum - numbers[idx])
    return ways