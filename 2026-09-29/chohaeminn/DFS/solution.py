"""
[풀이 접근]

한 번에 알파벳 하나만 바꿔 단어를 변환할 수 있다.
각 단어를 정점, 한 글자만 다른 단어 사이를 간선으로 보면
모든 변환 비용이 같은 최단 경로 문제이므로 BFS를 사용한다.

[자료구조]
- queue: 현재 단어와 변환 횟수를 저장하는 BFS 큐
- visited: 이미 확인한 단어를 저장하는 set

[알고리즘]
1. 시작 단어와 변환 횟수 0을 큐에 넣는다.
2. 큐에서 단어와 변환 횟수를 하나씩 꺼낸다.
3. 현재 단어가 target이면 변환 횟수를 반환한다.
4. words 중 방문하지 않았고 현재 단어와 한 글자만 다른 단어를 찾는다.
5. 해당 단어를 방문 처리하고, 변환 횟수를 1 증가시켜 큐에 넣는다.
6. 큐가 빌 때까지 target에 도달하지 못하면 0을 반환한다.

zip으로 두 단어의 각 글자를 비교한다.
서로 다른 글자의 개수가 1이면 변환 가능한 단어이다.

[복잡도]
- N: words의 단어 개수, L: 각 단어의 길이
- 시간 복잡도: O(N^2 * L)
- 공간 복잡도: O(N)
"""

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
