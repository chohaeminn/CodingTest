# [Programmers] H-Index

- **문제 링크**: [프로그래머스 > 정렬 > H-Index](https://school.programmers.co.kr/learn/courses/30/lessons/42748)
- **난이도**: Level 2
- **주제**: 정렬 (Sorting)

---

## 📌 문제 설명

H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 $h$를 구하려고 합니다. 위키백과에 따르면, H-Index는 다음과 같이 구합니다.

> 어떤 과학자가 발표한 논문 $n$편 중, **$h$번 이상 인용된 논문이 $h$편 이상**이고 나머지 논문이 $h$번 이하 인용되었다면 $h$의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 `citations`가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 `solution` 함수를 작성해주세요.

---

## 🔒 제한사항

- 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
- 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

---

## 💡 입출력 예

| citations         | return |
| :---------------- | :----- |
| `[3, 0, 6, 1, 5]` | `3`    |

### 입출력 예 설명

이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다. 그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 **3**입니다.

---

## 🧠 풀이 접근 법 (Algorithm)

1. **내림차순 정렬**:
   인용 횟수가 높은 논문부터 확인하기 위해 `citations` 배열을 내림차순으로 정렬합니다.
2. **조건 검사 (탈락 지점 탐색)**:
   정렬된 배열을 순회하면서 $i$번째 논문(0-indexed)의 인용 횟수(`citation`)가 고려 중인 논문 수(`i + 1`)보다 적어지는 지점을 찾습니다.
3. **리턴 로직**:
   - **중간 탈락 발생**: `citation < i + 1` (또는 `i >= citation`) 조건이 걸리는 즉시, 그 직전까지 조건을 만족했던 총 논문 수인 **`return i`**를 실행하고 함수를 종결합니다.
   - **탈락 없이 통과**: 모든 논문의 인용 횟수가 논문 수 이상이라 `if`문에 안 걸리고 `for`문이 끝나면, 전체 논문 개수인 **`return len(citations)`**를 반환합니다.

---

## 💻 Python 코드

```python
def solution(citations):
    # 1. 내림차순 정렬
    citations.sort(reverse=True)

    # 2. 순번(i + 1)과 인용 횟수(citation) 비교
    for i, citation in enumerate(citations):
        if citation < i + 1:
            return i  # 중간에 조건이 깨지면 탈락 지점(i) 즉시 반환 후 종료

    # 3. 모든 논문이 끝까지 조건을 만족하며 통과한 경우
    return len(citations)
```
