
""" [PCCP 모의고사 #2] 카페 확장 """

def solution(menu, order, k):
    answer = 0

    client = []
    start, end = -k, 0

    for idx in range(len(order)):

        start += k
        end = (start if end < start else end) + menu[order[idx]]
        client.append((start, end))

        count = 1
        for jdx in range(idx):
            if start < client[jdx][1]:
                count += 1
        
        answer = max(answer, count)

    return answer


print(solution([5, 12, 30], [1, 2, 0, 1], 10))                  # 3
print(solution([5, 12, 30], [2, 1, 0, 0, 0, 1, 0], 10))         # 4
print(solution([5], [0, 0, 0, 0, 0], 5))                        # 1

print(solution([5, 6, 7, 11], [1, 2, 3, 3, 2, 1, 1], 10))       # 2