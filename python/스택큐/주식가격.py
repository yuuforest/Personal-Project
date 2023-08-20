
""" Level 2. 주식가격 """

def solution(prices):

    length = len(prices)
    answer = [0 for _ in range(length)]

    for idx, price in enumerate(prices[:length-1]):
        
        i = idx+1

        while i < (length - 1) and price <= prices[i]:
            i += 1

        answer[idx] = i - idx

    return answer


print(solution([1, 2, 3, 2, 3]))        # [4, 3, 1, 1, 0]