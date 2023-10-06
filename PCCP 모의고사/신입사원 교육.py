
""" [PCCP 모의고사 #2] 신입사원 교육 """

from heapq import heappush, heappop

def solution(ability, number):

    q = []
    for a in ability:
        heappush(q, a)

    for _ in range(number):

        total = 0
        for _ in range(2):
            total += heappop(q)
        
        heappush(q, total)
        heappush(q, total)

    return sum(q)

print(solution([10, 3, 7, 2], 2))       # 37
print(solution([1, 2, 3, 4], 3))        # 26