# [BOJ] 9081. 단어 맞추기

import sys
input = sys.stdin.readline


def find(lst, l):
    # 마지막 단어인 경우
    if lst == sorted(lst, reverse=True):
        print(I)
        return

    # s = sorted(lst, reverse=True)
    
    for i in range(l - 2, -1, -1):
        check = lst[i:l]

        if check == sorted(check, reverse=True):
            continue

        else:
            s = sorted(check, reverse=True)
            ans = ""
            for j in range(l - 1, i - 1, -1):
                cur = lst[j:l]
                if cur == sorted(cur, reverse=True):
                    continue
                else:
                    for k in range(j):
                        ans += lst[k]
                    v = s[s.index(cur[0]) - 1]
                    ans += v
                    cur.pop(cur.index(v))

                    for ss in sorted(cur):
                        ans += ss
            print(ans)
            return  
          

T = int(input())
for tc in range(T):
    L = []
    I = input().rstrip()

    for i in I:
        L.append(i)

    find(L, len(L))
    
    
