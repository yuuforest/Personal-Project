
""" 레벨 2. 타겟 넘버 """

count = 0

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return count


def dfs(numbers, target, idx, sum):

    global count
    if idx == len(numbers):
        if sum == target:
            count += 1
        return
    
    dfs(numbers, target, idx+1, sum-numbers[idx])
    dfs(numbers, target, idx+1, sum+numbers[idx])


### 실행
print(solution([1, 1, 1, 1, 1], 3))     # 5
print(solution([4, 1, 2, 1], 4))        # 2