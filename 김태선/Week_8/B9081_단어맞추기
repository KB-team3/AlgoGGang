from sys import stdin

read = stdin.readline

for k in range(int(read())):
    word = list(read().rstrip())
    length = len(word)
    i, j = 0, 1

    # 바꿀 위치 찾는다.
    for idx in range(1, length):
        if word[idx] > word[idx - 1]:
            if i < idx:
                i = idx
    for idx in range(1, length):
        if word[idx] > word[i - 1]:
            if j < idx:
                j = idx

    if i != 0 and j != 0:
        word[i-1], word[j] = word[j], word[i-1]
        word[i:] = sorted(word[i:])
   
    print(''.join(word))