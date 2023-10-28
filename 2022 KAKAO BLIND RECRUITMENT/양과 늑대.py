
""" [2022 KAKAO BLIND RECRUITMENT] Level 3. 양과 늑대 """

from collections import deque

def solution(info, edges):

    # 익숙한 인접리스트를 만들자! 나는 배고프지 않다!
    graph = [[] for _ in range(len(info))]

    for edge in edges:
        graph[edge[0]].append(edge[1])

    return search(info, graph)

def search(info, graph):

    q = deque()

    answer = 0
    q.append((1, 0, graph[0]))

    while q:

        sheep, wolf, movePlace = q.popleft()

        answer = max(answer, sheep)

        for idx in range(len(movePlace)):

            node = movePlace[idx]

            nextSheep, nextWolf = sheep, wolf
            nextPlace = movePlace[:idx] + movePlace[idx+1:] + graph[node]
            
            if info[node] == 0:
                nextSheep += 1
            else:
                nextWolf += 1

            if nextSheep <= nextWolf:
                nextSheep = 0

            q.append((nextSheep, nextWolf, nextPlace))

    return answer


print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))       # 5
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))                # 5