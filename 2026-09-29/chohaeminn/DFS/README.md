# 단어 변환

- 문제: [프로그래머스 - 단어 변환](https://school.programmers.co.kr/learn/courses/30/lessons/43163)
- 분류: BFS, 그래프 탐색
- 사용 언어: Python

## 문제 요약

시작 단어 `begin`을 목표 단어 `target`으로 변환하는 최소 횟수를 구한다.

단어를 변환할 때는 다음 규칙을 따른다.

- 한 번에 한 개의 알파벳만 바꿀 수 있다.
- `words`에 있는 단어로만 변환할 수 있다.
- `target`으로 변환할 수 없으면 `0`을 반환한다.

## 풀이

각 단어를 그래프의 **정점**으로, 한 글자만 다른 두 단어의 관계를 **간선**으로 볼 수 있다.
모든 변환의 비용이 1로 같으므로, 최소 변환 횟수를 찾기 위해 BFS를 사용한다.

1. `target`이 `words`에 없으면 변환할 수 없으므로 `0`을 반환한다.
2. 큐에 `(begin, 0)`을 넣고 BFS를 시작한다.
3. 현재 단어와 `words`의 각 단어를 비교한다.
4. 방문하지 않은 단어 중 한 글자만 다른 단어를 큐에 넣는다.
5. `target`에 도달하면 현재까지의 변환 횟수를 반환한다.

## 핵심 로직

```python
difference = sum(
    a != b for a, b in zip(current, word)
)
```

`zip`으로 두 단어의 각 글자를 비교한다. 비교 결과가 다른 글자의 개수가 1이면 한 번에 변환할 수 있는 단어이다.

## 복잡도

`N`을 `words`의 단어 개수, `L`을 각 단어의 길이라고 하면:

- 시간 복잡도: **O(N² × L)**
  - 최대 `N`개의 단어를 방문한다.
  - 각 단어마다 `words` 전체 `N`개를 확인한다.
  - 두 단어의 연결 여부를 판단할 때 최대 `L`개의 글자를 비교한다.
- 공간 복잡도: **O(N)**
  - 큐와 방문 집합에 최대 `N`개의 단어가 저장된다.

## 풀이 코드

```python
from collections import deque


def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(begin, 0)])
    visited = {begin}

    while queue:
        current, step = queue.popleft()

        if current == target:
            return step

        for word in words:
            difference = sum(
                a != b for a, b in zip(current, word)
            )

            if word not in visited and difference == 1:
                visited.add(word)
                queue.append((word, step + 1))

    return 0
```
