
""" Level 3. 베스트앨범 """

from collections import defaultdict

def solution(genres, plays):

    answer = []

    count_genre = defaultdict(list)
    count_play = defaultdict(int)

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        count_play[genre] += play
        count_genre[genre].append((idx, play))

    for (g, _) in sorted(count_play.items(), key=lambda x:-x[1]):
        for (p, _) in sorted(count_genre[g], key=lambda x:(-x[1], x[0])) [:2]:
            answer.append(p)

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))    # [4, 1, 3, 0]

# print(solution(["classic", "pop", "classic", "classic"], [500, 600, 150, 800]))                 # [3, 0, 1]
# print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 500, 150, 2500]))    # [4, 1, 0, 2]