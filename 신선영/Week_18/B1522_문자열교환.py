import sys
input = sys.stdin.readline

s = input().rstrip()
ans = 1000
cnt = s.count('a')

s += s

for i in range(len(s) - cnt):
    ans = min(s[i:i + cnt].count('b'), ans)

print(ans)
