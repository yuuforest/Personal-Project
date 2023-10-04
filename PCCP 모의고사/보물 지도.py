
""" [PCCP 모의고사 #2] 보물 지도 """

from collections import deque

def solution(col, row, hole):
    
    graph = [[0] * col for _ in range(row)]
    for c, r in hole:   
        graph[abs(r-row)][c-1] = -1   # 함정 표시  

    visited = [[[0] * 2 for _ in range(col)] for _ in range(row)]
    visited[row-1][0][1] = True

    q = deque()
    q.append((row-1, 0, 1))

    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    
    answer = 0

    while q:

        for _ in range(len(q)):
            r, c, flag = q.popleft()

            if r == 0 and c == col-1:
                return answer

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]

                if 0 <= nr < row and 0 <= nc < col and not graph[nr][nc] and not visited[nr][nc][flag]:
                    visited[nr][nc][flag] = True
                    q.append((nr, nc, flag))
                
                if flag:
                    nr += dr[d]
                    nc += dc[d]
                    if 0 <= nr < row and 0 <= nc < col and not graph[nr][nc] and not visited[nr][nc][0]:
                        visited[nr][nc][0] = True
                        q.append((nr, nc, 0))

        answer += 1

    return -1


print(solution(4, 4, [[2, 3], [3, 3]]))                                                                 # 5
print(solution(5, 4, [[1, 4], [2, 1], [2, 2], [2, 3], [2, 4], [3, 3], [4, 1], [4, 3], [5, 3]]))         # -1