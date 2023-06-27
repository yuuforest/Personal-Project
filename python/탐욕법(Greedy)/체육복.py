
""" Level 1. 체육복 """

def solution(n, lost, reserve):
    answer = 0
    
    nlost = list(set(lost) - set(reserve))
    nreserve = set(reserve) - set(lost)
    
    nlost.sort()
    
    for num in nlost:
        if num-1 in nreserve:
            nreserve.remove(num-1)
        elif num+1 in nreserve:
            nreserve.remove(num+1)
        else:
            answer += 1
        
    return n - answer

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))