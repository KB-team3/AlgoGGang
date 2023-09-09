from sys import stdin
input = stdin.readline

s = input().strip()
a = s.count('a')

s += s[0:a - 1]     # 원형 처리
min_val = float(1e9)

for i in range(len(s) - (a - 1)) : 
    min_val = min(min_val, s[i:i + a].count('b'))

print(min_val)