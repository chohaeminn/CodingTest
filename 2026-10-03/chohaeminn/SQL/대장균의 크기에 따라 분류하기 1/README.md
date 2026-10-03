# SQL 대장균의 크기에 따라 분류하기

## 문제 정보

- 출처: 프로그래머스
- 단계: Level 2
- 사용 테이블: ECOLI_DATA

---

## 문제 설명

대장균 개체의 크기(SIZE_OF_COLONY)에 따라 세가지 구간으로 분류하는 문제입니다.

- 100 이하: 'LOW'
- 100 초과 1000 이하: 'MEDIUM'
- 1000 초과: 'HIGH'

모든 대장균 개체의 ID(ID)와 분류된 이름(SIZE)을 출력하며, 결과는 개체의 ID에 대해 오름차순 정렬해야 합니다.

---

## 정답 SQL 쿼리

```sql
SELECT ID,
CASE
    WHEN SIZE_OF_COLONY <= 100 THEN 'LOW'
    WHEN (SIZE_OF_COLONY > 100) AND (SIZE_OF_COLONY <= 1000) THEN 'MEDIUM'
    WHEN SIZE_OF_COLONY > 1000 THEN 'HIGH'
    END AS SIZE
FROM ECOLI_DATA
ORDER BY ID ASC;
```
