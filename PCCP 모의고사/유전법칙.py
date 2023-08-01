
""" [PCCP 모의고사 #1] 유전법칙 """
    
def spread(generation, order):
    stack = []

    order -= 1
    while generation > 1:
        generation -= 1
        stack.append(order % 4)
        order //= 4

    while stack:
        number = stack.pop()
        if number == 0:
            return "RR"
        if number == 3:
            return "rr"
    return "Rr"
    


def solution(queries):
    answer = []

    for generation, order in queries:    # 완두콩의 세대, 세대 내에서 개체 순서
        answer.append(spread(generation, order))

    return answer


print(solution([[3, 5]]))                           # ["RR"]
print(solution([[3, 8], [2, 2]]))                   # ["rr", "Rr"]
print(solution([[3, 1], [2, 3], [3, 9]]))         # ["RR", "Rr", "RR"]
print(solution([[4, 26]]))                        # ["Rr"]