
""" 레벨 2. 가장 큰 정사각형 찾기 """

def solution(board):

    answer = 0

    for r in range(0, len(board)):
        for c in range(0, len(board[0])):

            if r > 0 and c > 0 and board[r][c] == 1:
                board[r][c] += min(board[r-1][c-1], board[r-1][c], board[r][c-1])

            answer = max(board[r][c], answer)

    print(board)

    return answer ** 2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))                          # 9
print(solution([[0,0,1,1],[1,1,1,1]]))                                              # 4

print(solution([[0,1,0,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[0,0,1,1,0]]))      # 9
print(solution([[0, 1, 1, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]))              # 1
print(solution([[0, 0, 0, 0],[1, 0, 0, 0],[1, 0, 0, 0],[0, 0, 0, 0]]))              # 1
print(solution([[1,1,1],[1,0,1],[1,1,1]]))                                          # 1