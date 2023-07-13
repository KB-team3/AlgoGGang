N = int(input())
arr = list(map(int, input().split(" ")))
ans_arr = [i for i in range(N)]
ans = [0 for _ in range(N)]
for i, num in enumerate(arr):
    ans[ans_arr.pop(num)]=i+1
print("".join(str(s)+" " for s in ans))