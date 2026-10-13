def solution(genres, plays):
    answer = []

    genre_total_play = {}
    genre_songs = {}

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        if genre in genre_total_play:
            genre_total_play[genre] += play
        else:
            genre_total_play[genre] = play

        if genre in genre_songs:
            genre_songs[genre].append((i,play))
        else:
            genre_songs[genre] = [(i,play)]

    sorted_genres = sorted(genre_total_play.items(), key=lamda x: x[1], reverse = True)

    for genre, total_play in sorted_genres:
        sorted_songs = sorted(genre_songs[genre], key=lamda x: (-x[1], x[0]))

        for i in range(min, (2, len(sorted_songs))):
            answer.append(sorted_songs[i][0])
    return answer
