# [프로그래머스] 자동차 평균 대여 기간 구하기 (Lv.2)

- **문제 링크:** [프로그래머스 - 자동차 평균 대여 기간 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/157342)
- **카테고리:** `STRING, DATE` / `GROUP BY`
- **사용 언어:** `MySQL`

---

## 📌 문제 요약

`CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블에서 **평균 대여 기간이 7일 이상**인 자동차들의 `CAR_ID`와 평균 대여 기간(`AVERAGE_DURATION`)을 조회하는 SQL문을 작성합니다.

### 조건

1. 평균 대여 기간은 **소수점 두 번째 자리에서 반올림** (소수점 첫째 자리까지 표기)
2. 결과는 **평균 대여 기간 기준 내림차순** 정렬
3. 평균 대여 기간이 같다면 **자동차 ID 기준 내림차순** 정렬

---

## 💡 풀이 핵심 & 회고

### 1. 대여 기간 계산 시 `+ 1` 처리

- 당일 대여 후 당일 반납(`START_DATE` = `END_DATE`)의 경우 대여 기간은 **1일**입니다.
- `DATEDIFF(END_DATE, START_DATE)`는 단순 일수 차이(`0`)만 반환하므로 반드시 **`+ 1`**을 더해야 합니다.

### 2. `DATEDIFF` 함수 문법 주의 (MySQL)

- 언더바(`_`) 없이 `DATEDIFF`로 작성합니다.
- `DATEDIFF(종료일, 시작일)` 순서로 인자를 넣어야 양수 값이 반환됩니다. _(시작일을 먼저 넣으면 음수 발생)_

### 3. 반올림 자릿수 및 `HAVING` 필터링

- *"소수점 두 번째 자리에서 반올림"*은 첫째 자리까지 표시하는 것이므로 `ROUND(..., 1)`을 사용합니다.
- `GROUP BY`로 그룹화된 집계 결과에 조건을 걸 때는 `WHERE`가 아닌 **`HAVING`** 절을 사용합니다.

---

## ✅ 정답 코드 (MySQL)

```sql
SELECT
    CAR_ID,
    ROUND(AVG(DATEDIFF(END_DATE, START_DATE) + 1), 1) AS AVERAGE_DURATION
FROM
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY
    CAR_ID
HAVING
    AVERAGE_DURATION >= 7
ORDER BY
    AVERAGE_DURATION DESC,
    CAR_ID DESC;
```
