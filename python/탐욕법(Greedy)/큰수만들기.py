
""" Level 2. 큰 수 만들기 """

def solution(number, k):
    answer = []

    count_remove = 0
    Length = len(number) - k
    
    for num in range(0, len(number)):

        temp = number[num]

        if not answer or count_remove >= k:
            answer.append(temp)
            continue

        while answer and answer[-1] < temp and count_remove < k:
            answer.pop()
            count_remove += 1

        if len(answer) < Length:
            answer.append(temp)
        
    return ''.join(answer)

print(solution("1924", 2))              # "94"
print(solution("1231234",3))            # "3234"
print(solution("4177252841", 4))        # "775841"

print(solution("1924", 3))              # "9"
print(solution("1231234",6))            # "4"
print(solution("4177252841", 9))        # "8"