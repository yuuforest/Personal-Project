
""" [PCCP 모의고사 #1] 운영체제 """

def solution(program):
    answer = [0 for _ in range(11)]

    program.sort(key=lambda x: (x[1], x[0]))    # 호출된 시각과 우선순위를 기준으로 정렬



    return answer


# [우선순위, 호출된 시각, 실행 시간]
print(solution([[2, 0, 10], [1, 5, 5], [3, 5, 3], [3, 12, 2]]))     # [20, 5, 0, 16, 0, 0, 0, 0, 0, 0, 0]
print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))       # [19, 0, 0, 4, 3, 14, 0, 0, 0, 0, 0]