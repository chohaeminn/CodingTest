# 프로그래머스 - 베스트앨범 (Best Album)

## 문제 설명

스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 수록 기준은 다음과 같습니다.

1. 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
2. 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
3. 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.

---

## 접근 방식 (왜 해시를 사용해야 하는가?)

이 문제를 해결하기 위해서는 두 가지 데이터를 효율적으로 관리해야 합니다.

1. 장르별 총 재생 횟수: 어떤 장르가 가장 많이 재생되었는지 순위를 매겨야 합니다.
2. 장르별 노래 목록 관리: 각 장르에 속한 노래들의 [고유 번호, 재생 횟수]를 모아두고 조건에 맞게 정렬해야 합니다.

- 해시(파이썬 dict)의 장점: 장르 이름(Key)만으로 총 재생 횟수와 해당 장르의 노래 목록(Value)에 O(1) 시간 만에 접근할 수 있어, 데이터를 그룹화하고 집계하는 작업을 매우 빠르고 직관적으로 처리할 수 있습니다.

---

## 시간 복잡도 분석 (O(N log N))

전체 노래의 개수를 N, 장르의 개수를 G라고 할 때:

1. 해시 구성: N개의 노래를 순회하며 장르별 총 재생 횟수와 노래 정보를 저장합니다. -> O(N)
2. 장르 정렬: 장르의 총 재생 횟수를 기준으로 장르들을 내림차순 정렬합니다. (G는 최대 100개 미만) -> O(G log G)
3. 장르 내 노래 정렬 및 추출: 각 장르별로 노래를 정렬합니다. 각 장르의 노래 수를 N1, N2, ...라 할 때, 개별 정렬의 합은 전체 데이터를 한 번에 정렬하는 것보다 클 수 없으므로 전체 복잡도는 O(N log N)을 넘지 않습니다. -> O(N log N)

최종 시간 복잡도는 O(N log N)이며, N <= 10,000이므로 제한 시간 내에 아주 넉넉하게 통과합니다.

---

## 전체 Python 코드

```python
def solution(genres, plays):
    answer = []

    # 1. 장르별 총 재생 횟수를 저장할 딕셔너리
    genre_total_play = {}
    # 2. 장르별 노래 정보([고유번호, 재생횟수])를 저장할 딕셔너리
    genre_songs = {}

    # [1단계] 데이터를 순회하며 해시(딕셔너리) 채우기
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]

        # 장르별 총 재생 횟수 누적
        if genre in genre_total_play:
            genre_total_play[genre] += play
        else:
            genre_total_play[genre] = play

        # 장르별 노래 목록에 추가 (고유 번호와 재생 횟수 저장)
        if genre in genre_songs:
            genre_songs[genre].append((i, play))
        else:
            genre_songs[genre] = [(i, play)]

    # [2단계] 총 재생 횟수가 많은 장르 순으로 정렬 (내림차순)
    sorted_genres = sorted(genre_total_play.items(), key=lambda x: x[1], reverse=True)

    # [3단계] 장르별로 노래를 정렬하고 최대 2곡씩 뽑아 정답에 추가
    for genre, total_play in sorted_genres:
        # 1순위: 재생 횟수 내림차순(-x[1]) / 2순위: 고유 번호 오름차순(x[0])
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[1], x[0]))

        # 최대 2곡까지 안전하게 반복하며 고유 번호만 추출
        for i in range(min(2, len(sorted_songs))):
            answer.append(sorted_songs[i][0])

    return answer
```
