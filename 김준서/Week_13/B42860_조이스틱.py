ss = 'ABCDEFGHIJKLM'
sa = 'NOPQRSTUVWXYZA'
def solution(name):
    li = []
    N = len(name)
    if name.count('A')==N:
        return 0
    dic = {s: i for i, s in enumerate(ss)}
    for i, s in enumerate(reversed(sa)):
        dic[s] = i
    answer = N-1
    plus = dic[name[0]]
    name = 'A'+name[1:]
    def find(idx):
        ret = [None, None]
        p = idx-1
        while p>=0:
            if name[p]!='A':
                ret[0]=p
                break
            p -=1
        p = idx+1
        while p<N:
            if name[p]!='A':
                ret[1]=p
                break
            p +=1
        return ret
    for i, s in enumerate(name):
        if s!='A':
            left, right = find(i)
            answer = min(answer, N-i if left==None else left+2*(N-i))
            answer = min(answer, i if right == None else N-right+2*i)
    for s in name:
        answer += dic[s]
    return answer+plus