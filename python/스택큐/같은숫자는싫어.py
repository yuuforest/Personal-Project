
""" Level 1. 같은 숫자는 싫어 """

def solution(arr):
    answer = []

    answer.append(arr[0])
    previous = arr[0]

    for num in arr[1:]:

        if previous != num:
            answer.append(num)
            previous = num
        
    return answer


print(solution([1,1,3,3,0,1,1]))        # [1,3,0,1]
print(solution([4,4,4,3,3]))            # [4,3]