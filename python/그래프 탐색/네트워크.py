
""" 레벨 3. 네트워크 """

def solution(n, computers):
    answer = 0
    visited = [False] * n

    for idx in range(n):
        if not visited[idx]:
            answer += 1
            dfs(n, computers, idx, visited)

    return answer


def dfs(n, computers, node, visited):

    visited[node] = True

    for com in range(n):
        if not visited[com] and computers[node][com]:
            dfs(n, computers, com, visited)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))       # 2
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))       # 1