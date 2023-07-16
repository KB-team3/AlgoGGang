import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
arr = []

for i in range(n):
    arr.append((nums[i],i+1))
arr.sort(key = lambda x : (x[0],-x[1]))

ans = []
for a,b in arr:
    cnt = 0
    for i in range(len(arr)):
        if a == cnt:
            ans.insert(i,b)
            break
        if ans[i] > b:
            cnt += 1
print(*arr)