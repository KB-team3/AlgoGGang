def solution(name):
    def get_min_moves(name, index):
        # 현재 위치의 알파벳 조작 횟수
        move = min(ord(name[index]) - ord('A'), ord('Z') - ord(name[index]) + 1)
        
        # 현재 위치에서 왼쪽으로 이동하는 횟수
        left = 1
        while name[index - left] == 'A':
            left += 1
        
        # 현재 위치에서 오른쪽으로 이동하는 횟수
        right = 1
        while name[(index + right) % len(name)] == 'A':
            right += 1
        
        # 최소 이동 횟수 계산
        min_moves = move
        next_index = (index + right) % len(name)
        if right > left:
            min_moves += get_min_moves(name, (index - left) % len(name))
        else:
            min_moves += get_min_moves(name, next_index)
        
        return min_moves
    
    # 시작은 첫 문자부터
    answer = get_min_moves(name, 0)
    return answer