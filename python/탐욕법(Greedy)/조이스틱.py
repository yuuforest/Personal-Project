
""" Level 2. 조이스틱 """

def solution(name):
    answer = 0

    # ord("A") = 65     ord("J") - 65 = 9

    for num, char in enumerate(name):   # J A Z

        # 알파벳 변경 ord("A") = 65, ord("Z") = 90
        answer += min(ord(char) - 65, 90 - ord(char) + 1)

        # 위치 이동

    return answer

# print(solution("JEROEN"))   # 56
# print(solution("JAN"))      # 23
print(solution("JAZ"))      # 11