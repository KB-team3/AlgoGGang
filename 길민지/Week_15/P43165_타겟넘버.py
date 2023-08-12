def func(numbers, target, i, cnt):
    ans = 0
    if (i == len(numbers)):
        if(cnt == target):
            return 1;
        return 0;
    ans += func(numbers, target, i+1, cnt+numbers[i]);
    ans += func(numbers, target, i+1, cnt-numbers[i]);
    return ans;
    
def solution(numbers, target):
    answer = func(numbers, target, 0, 0);
    return answer