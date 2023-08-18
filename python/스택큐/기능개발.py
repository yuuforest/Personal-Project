
""" Level 2. 기능개발 """

def solution(progresses, speeds):
    answer = []

    P = []
    for idx in range(len(progresses)):
        n, r = divmod(100 - progresses[idx], speeds[idx])
        P.append(n+1 if r else n)

    temp = P[0]
    count = 1

    for p in P[1:]:

        if p <= temp:
            count += 1
        else:
            answer.append(count)
            temp = p
            count = 1

    if count:
        answer.append(count)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))                           # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))       # [1, 3, 2]