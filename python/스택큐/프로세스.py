
""" Level 2. 프로세스 """

def solution(priorities, location):
    answer = 0

    P = []

    for idx, pr in enumerate(priorities):
        P.append((pr, idx))

    while P:
        
        temp = P.pop(0)

        if P and temp[0] < max(P)[0]:
            P.append(temp)
            continue

        answer += 1

        if temp[1] == location:
            break

    return answer

# print(solution([2, 1, 3, 2], 2))            # 1
# print(solution([1, 1, 9, 1, 1, 1], 0))      # 5

print(solution([1, 1, 1, 2], 2))            # 4