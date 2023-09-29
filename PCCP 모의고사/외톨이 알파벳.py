
""" [PCCP 모의고사 #1] 외톨이 알파벳 """

def solution(input_string):
    
    idx = 0
    count = {}
    
    length = len(input_string)

    while idx < length:
        
        now = input_string[idx]
        count[now] = count.setdefault(now, 0) + 1

        while idx < length and input_string[idx] == now:
            idx += 1

    answer = ''
    for c in count:
        if count.get(c) > 1:
            answer += c

    return "".join(sorted(answer)) if answer else "N"


print(solution("edeaaabbccd"))      # "de"
print(solution("eeddee"))           # "e"
print(solution("string"))           # "N"
print(solution("zbzbz"))            # "bz"