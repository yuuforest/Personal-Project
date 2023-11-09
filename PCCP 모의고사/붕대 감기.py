
""" [PCCP 기출문제 #1] 붕대 감기 """

def solution(bandage, health, attacks):

    # bandage : 시전 시간, 초당 회복량, 추가 회복량
    # health : 최대 최력
    # attacks : 몬스터의 공격 시간과 피해량

    previous_time = 0
    now = health
    
    for (attack_time, attack_amount) in attacks:
        
        time = attack_time - previous_time - 1

        now += time * bandage[1] + (time // bandage[0]) * bandage[2]

        if health < now:
            now = health

        now -= attack_amount

        if now <= 0:
            return -1
        
        previous_time = attack_time
    
    return now

print(solution([5, 1, 5], 30, [[2, 10], [9, 15], [10, 5], [11, 5]]))    # 5
print(solution([3, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))              # -1
print(solution([4, 2, 7], 20, [[1, 15], [5, 16], [8, 6]]))              # -1
print(solution([1, 1, 1], 5, [[1, 2], [3, 2]]))                         # 3