
""" [PCCP 기출문제 #2] 가장 많은 석유 """

from collections import deque

def solution(land):

    # 0이면 빈 땅, 1이면 석유가 있는 땅
    R, C = len(land), len(land[0])

    answer = [0] * len(land[0])

    for r in range(R):
        for c in range(C):
            if land[r][c] == 1:
                land, total_column, oil_land = search(land, R, C, r, c)
                for t in total_column:
                    answer[t] += oil_land

    return max(answer)

def search(land, R, C, r, c):

    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]

    q = deque()

    q.append((r, c))
    land[r][c] = 0
    
    total_column = set()
    total_column.add(c)

    oil_land = 0

    while q:

        r, c = q.popleft()

        oil_land += 1

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nc < 0 or nr >= R or nc >= C or land[nr][nc] == 0:
                continue

            q.append((nr, nc))
            land[nr][nc] = 0

            if nc not in total_column:
                total_column.add(nc)
    
    return land, total_column, oil_land

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))                 # 9
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))       # 16