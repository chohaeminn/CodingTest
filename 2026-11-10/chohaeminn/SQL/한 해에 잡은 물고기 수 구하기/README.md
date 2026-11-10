# [Programmers] 2021년에 잡은 물고기 수 구하기

### 🔗 문제 링크

[프로그래머스 - 2021년에 잡은 물고기 수 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/298516)

---

### 📌 문제 설명

`FISH_INFO` 테이블에서 **2021년도에 잡은 물고기의 수**를 출력하는 SQL 문을 작성합니다.

- 결과 컬럼명은 `FISH_COUNT`로 지정합니다.

---

### 💡 풀이 과정

1. **연도 조건 필터링**: `TIME` 컬럼(DATE/DATETIME)에서 `YEAR()` 함수를 사용하여 연도가 `2021`인 행만 추출합니다.
2. **개수 집계**: 조건에 해당하는 물고기 수를 구하기 위해 `COUNT(*)` 함수를 적용합니다.
3. **컬럼명 지정**: 문제 조건에 따라 별칭(`AS`)을 이용해 결과를 `FISH_COUNT`로 출력합니다.

---

### 💻 SQL 코드

```sql
SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO
WHERE YEAR(TIME) = 2021;
```
