# 소수 찾기

## 1. 문제 개요

- **출처:** 프로그래머스 (완전탐색)
- **설명:** 한 자리 숫자가 적힌 종이 조각을 붙여 만들 수 있는 소수의 총개수를 구하는 문제입니다.
- **제한사항:**
  - `numbers`는 길이 1 이상 7 이하인 문자열입니다.
  - `numbers`는 0~9까지의 숫자만으로 이루어져 있습니다.
  - `"011"`과 `"11"`은 같은 숫자로 취급합니다.

---

## 2. 접근 방법

### 숫자 조합 생성 (순열 및 집합)

- **순열(Permutation):** 종이 조각을 뽑는 순서에 따라 다른 숫자가 되므로(`17`과 `71`), `itertools.permutations`를 사용해 1자리부터 전체 길이까지 모든 순열을 생성합니다.
- **중복 제거(Set):** `"011"`과 `"11"`을 동일하게 처리하기 위해 생성된 문자열을 `int`형으로 변환한 뒤 `set`에 저장하여 앞자리의 불필요한 `0`과 중복된 숫자를 제거합니다.
- **시간 복잡도 타당성:** 입력 길이가 최대 7이므로 생성 가능한 순열은 최대 13,699개입니다. 완전탐색으로 모든 경우를 확인해도 제한 시간 내에 충분히 동작합니다.

### 소수 판별 (제곱근 활용)

- **제곱근 판별:** 어떤 수 $N$이 합성수라면 약수 중 적어도 하나는 반드시 $\sqrt{N}$ 이하에 존재합니다. 따라서 $2$부터 $\sqrt{N}$까지만 나누어 떨어지는지 검사하여 연산 횟수를 줄입니다.
- **예외 처리:** $2$ 미만의 수(`0`, `1`)는 소수가 아니므로 즉시 `False`를 반환합니다.

---

## 3. 코드 (Python)

```python
from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    candidates = set()

    for length in range(1, len(numbers) + 1):
        for p in permutations(numbers, length):
            num = int("".join(p))
            candidates.add(num)

    answer = sum(1 for num in candidates if is_prime(num))
    return answer
```
