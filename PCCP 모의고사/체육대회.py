
""" [PCCP 모의고사 #1] 체육대회 """

def solution(ability):
    answer = 0

    game = len(ability[0])

    ab = [[] for _ in range(game)]      # 게임별 학생의 능력치

    for i in range(len(ability)):
        for j in range(game):
            ab[j].append((i, ability[i][j]))

    for i in range(game):
        ab[i].sort(key=lambda x: x[1], reverse=True)
    
    print(ab)
    return answer

print(solution([[40, 10, 10], [20, 5, 0], [30, 30, 30], [70, 0, 70], [100, 100, 100]]))     # 210
# print(solution([[20, 30], [30, 20], [20, 30]]))                                             # 60