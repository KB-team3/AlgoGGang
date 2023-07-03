import copy
from collections import deque
N, M = map(int,input().split(" "))
board = [["_" for _ in range(M)] for _ in range(N)]
for i in range(N):
    temp = input()
    board[i] = [t for t in temp]
#갈 수 있으면 1, 구멍에 들어갔으면 2, 다른거 지나갔으면 3, 못가면 0
def isOk(board, loc):
    if board[loc[0]][loc[1]]=='.':
        return 1
    elif board[loc[0]][loc[1]]=='O':
        return 2
    elif board[loc[0]][loc[1]]=='#':
        return 0
    else: return 3
# 성공하면 True, 실패하면 False, 그냥 괜찮으면 board
def tilt(dir, board):
    global N, M
    dx, dy = [-1,0,1,0],[0,1,0,-1]
    bLoc, rLoc= [], []
    for i in range(N):
        for j in range(M):
            if board[i][j]=='B':
                bLoc = [i,j]
            elif board[i][j]=='R':
                rLoc = [i,j]
    B = [bLoc[0]+dx[dir],bLoc[1]+dy[dir]]
    B_passed = False
    while True:
        temp=isOk(board, B)
        if temp==0:
            B[0]-=dx[dir]
            B[1]-=dy[dir]
            break
        elif temp==2:
            return False
        elif temp==3:
            B_passed = True
        B[0]+=dx[dir]
        B[1]+=dy[dir]
    if B_passed:
        B[0]-=dx[dir]
        B[1]-=dy[dir]
    R = [rLoc[0]+dx[dir],rLoc[1]+dy[dir]]
    R_passed = False
    while True:
        temp = isOk(board, R)
        if temp==0:
            R[0]-=dx[dir]
            R[1]-=dy[dir]
            break
        elif temp==2:
            return True
        elif temp ==3:
            R_passed = True
        R[0]+=dx[dir]
        R[1]+=dy[dir]
    if R_passed:
        R[0]-=dx[dir]
        R[1]-=dy[dir]
    ret_board =copy.deepcopy(board)
    ret_board[bLoc[0]][bLoc[1]]='.'
    ret_board[rLoc[0]][rLoc[1]]='.'
    ret_board[R[0]][R[1]]='R'
    ret_board[B[0]][B[1]]='B'
    return ret_board
def board2str(board):
    ret = ""
    for b in board:
        temp = "".join(b)
        ret+=temp
    return ret
def bfs():
    queue = deque()
    queue.append([board, 0])
    visited = dict()
    visited[board2str(board)]=True
    while queue:
        temp_board, count = queue.popleft()
        for i in range(4):
            ret_temp = tilt(i, temp_board)
            if ret_temp == True:
                return count+1
            elif ret_temp == False or count+1==11:
                continue
            vi=board2str(ret_temp)
            if vi not in visited:
                visited[vi]=True
                queue.append([ret_temp,count+1])
    return -1
print(bfs())