# [Python] 같은 숫자는 싫어 (스택/큐)

## 📌 문제 설명

배열 `arr`가 주어집니다. 배열 `arr`의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 이때, 배열 `arr`에서 **연속적으로 나타나는 숫자는 하나만 남기고 전부 제거**하려고 합니다. 단, 제거된 후 남은 수들을 반환할 때는 배열 `arr` 원소들의 순서를 유지해야 합니다.

- **제한사항**
  - 배열 `arr`의 크기 : 1,000,000 이하의 자연수
  - 배열 `arr`의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수

---

## 💡 정답 파이썬 코드 (`solution.py`)

```python
def solution(arr):
    answer = []

    for num in arr:
        # answer가 비어있지 않고, 스택의 마지막 값(직전 값)과 현재 값이 다를 때만 추가
        if not answer or answer[-1] != num:
            answer.append(num)

    return answer
```
