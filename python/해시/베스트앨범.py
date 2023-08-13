
""" Level 3. 베스트앨범 """

def solution(genres, plays):

    answer = []

    Music = {}

    for idx in range(len(genres)):

        genre = genres[idx]
        play = plays[idx]

        Music.setdefault(genre, [0])
        Music[genre][0] += play
        Music[genre].append((play, idx))

    Music = sorted(Music.items(), key=lambda x: x[1][0], reverse=True)

    for music in Music:
        
        
        print(music[1])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))        # [4, 1, 3, 0]