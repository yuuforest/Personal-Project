
""" [PCCP 모의고사 #2] 실습용 로봇 """

def solution(command):
    answer = [0, 0]

    dir = 0     # 위 0 오른쪽 1 아래 2 왼쪽 3

    for c in command:
        
        if c == 'R':
            dir = moveR(dir)
        elif c == 'L':
            dir = moveL(dir)
        elif c == 'G':
            answer = moveG(answer[0], answer[1], dir)
        else:
            answer = moveB(answer[0], answer[1], dir)
    
    return list(answer)

def moveR(dir):
    return (dir + 1) % 4

def moveL(dir):
    return 3 if dir-1 < 0 else dir-1

def moveG(x, y, dir):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    return x + dx[dir], y + dy[dir]

def moveB(x, y, dir):
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    return x + dx[dir], y + dy[dir]

print(solution("GRGLGRG"))      # [2, 2]
print(solution("GRGRGRB"))      # [2, 0]
