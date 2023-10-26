
""" 레벨 2. 가장 큰 정사각형 찾기 """

def solution(board):

    lenr = len(board)
    lenc = len(board[0])

    table = [[] for _ in range(len(board[0]))]

    for c in range(lenc):

        start, end = 0, 0

        while end < lenr:

            start = end
            while start < lenr and board[start][c] == 0:
                start += 1

            end = start
            while end < lenr and board[end][c] == 1:
                end += 1

            if board[end-1][c] == 1:
                table[c].append((start, end-1))

    return 0

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))                          # 9
# print(solution([[0,0,1,1],[1,1,1,1]]))                                              # 4

# print(solution([[0,1,0,0,0],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[0,0,1,1,0]]))      # 9