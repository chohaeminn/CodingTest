# 전화번호 목록 (Phone Number List)

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하는 문제의 풀이 및 접근 방식 설명입니다.

---

## 접근 방식 비교: 해시(Hash) vs 정렬(Sorting)

### 1. 왜 해시(Hash / Set)를 쓰는가?

- **상황:** 데이터의 개수가 최대 1,000,000개로 매우 많을 때, 단순 반복문(O(N^2))을 쓰면 연산 횟수가 1조 번에 달해 시간 초과가 발생합니다.
- **이유:** "내가 만든 이 접두어가 전체 전화번호부에 존재하는가?"라는 존재 여부 확인(Membership Check)을 O(1)의 속도로 빠르게 해결하기 위해 해시셋(set)을 사용합니다.
- **해시 풀이 코드:**
  ```python
  def solution(phone_book):
      phone_set = set(phone_book)
      for phone in phone_book:
          prefix = ""
          for digit in phone[:-1]:
              prefix += digit
              if prefix in phone_set:
                  return False
          return True
  ```
