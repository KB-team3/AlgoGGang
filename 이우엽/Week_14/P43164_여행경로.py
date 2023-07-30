tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
dict = {}
cur = []
answer = []
def dfs(k):
    cur.append(k)
    val = dict.get(k)
    if len(cur) == len(dict):
        print("cur", cur)
        answer.append(cur)
        return
    # if v in val: 여기서 왜 에러가 나는지 모르겠다
    #     print(v)
def solution(tickets):
    for ticket in tickets:
        start = ticket[0]
        end = ticket[1]
        if start in dict:
            dict.get(start).append(end)
        else:
            print("first")
            ends = []
            ends.append(end)
            dict[start] = ends
    # test 출력
    for key in dict:
        print(key, ":", dict.get(key))

    for key in dict:
        if len(cur) == 0 and key == "ICN":
            dfs(key)

    print("answer", answer)
    return answer

solution(tickets)