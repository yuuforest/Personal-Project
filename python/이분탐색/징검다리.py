
""" 레벨 4. 징검다리 """

def solution(distance, rocks, n):
    answer = 0

    rocks = [0] + sorted(rocks) + [distance]

    answer, start, end = 0, 0, distance

    while start <= end:
        mid = (start + end) // 2

        count, i = 0, 0
        for idx in range(1, len(rocks)):
            if rocks[idx] - rocks[i] < mid:
                count += 1
            else:
                i = idx

        if count == n:
            answer = max(mid, answer)
            break
        elif count < n:
            start = mid + 1
        else:
            end = mid - 1

    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))     # 4

print(solution(16, [4, 8, 11], 2))              # 8