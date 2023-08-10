vowels = 'AEIOU'
cnt = 0
g_word = ""
res = 0
def dfs(s):
    global cnt, res
    if s == g_word:
        print("res:", cnt)
        res = cnt
        return

    cnt += 1
    # print(s)
    # 종료조건
    if len(s) == 5:
        return
    # 재귀적 확장
    for vowel in vowels:
        dfs(s+vowel)
        s[:-1]
def solution(word):
    global g_word
    g_word = word
    dfs("")
    print("cnt:", cnt)
    return res