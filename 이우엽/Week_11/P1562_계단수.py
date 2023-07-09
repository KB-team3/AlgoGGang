N = int(input())

M = [0] * (N+1)
cnts = [0] * (N+1)
# print("M:", M)
def dp(x):
    if x == 2:
        cnt = 0
        mem = []
        for num in range(10, 100):
            num_str = str(num)
            l = list(num_str)
            # print(l)
            if abs(int(l[0]) - int(l[1])) == 1:
                # print(l)
                mem.append(l)
                cnt += 1
        # print(cnt)
        # print("mem:", mem)
        M[x] = mem
        cnts[x] = cnt
        return
    if x == 3:
        arr = []
        cnt = 0
        for mem in M[x-1]:
            for num in range(1, 10):
                if abs(num - int(mem[0])) == 1:
                    # print("mem[0]:", mem[0])
                    cnt += 1
                    arr.append(num)
        # print("arr:", arr)
        M[x] = arr
        cnts[x] = cnt * cnts[x-1]
        return
    if M[x] != 0:
        return M[x]
    arr = []
    cnt = 0
    for mem in M[x-1]:
        for num in range(1, 10):
            if abs(num - mem) == 1:
                # print("mem[0]:", mem[0])
                cnt += 1
                arr.append(num)
    # print("arr:", arr)
    M[x] = arr
    cnts[x] = cnt * cnts[x-1]
    return

for i in range(2, 11):
    dp(i)
print(cnts[10] % 1000000000)

# print(M)
# print(cnts)