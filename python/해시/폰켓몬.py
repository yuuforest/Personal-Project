
""" 레벨 1. 폰켓몬 """

def solution(nums):
    
    mons = set()
    for n in nums:
        mons.add(n)

    count = len(nums) // 2
    return count if count <= len(mons) else len(mons)

print(solution([3,1,2,3]))          # 2
print(solution([3,3,3,2,2,4]))      # 3
print(solution([3,3,3,2,2,2]))      # 2