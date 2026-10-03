# SQL 대장균들의 자식의 수 구하기

## 문제 정보

- 출처: 프로그래머스
- 단계: Level 2
- 사용 테이블: ECOLI_DATA

---

## 문제 설명

대장균들은 일정 주기로 분화하며, 분화를 시작한 개체를 부모 개체(PARENT_ID), 분화가 되어 나온 개체를 자식 개체라고 합니다.
모든 대장균 개체의 ID(ID)와 자식의 수(CHILD_COUNT)를 출력하는 SQL 문을 작성하는 문제입니다.

- 조건 1: 자식이 없다면 자식의 수는 0으로 출력해야 합니다.
- 조건 2: 결과는 개체의 ID에 대해 오름차순 정렬해야 합니다.

---

## 정답 SQL 쿼리

```sql
SELECT
    ID,
    (SELECT COUNT(*) FROM ECOLI_DATA WHERE PARENT_ID = A.ID) AS CHILD_COUNT
FROM
    ECOLI_DATA A
ORDER BY
    ID ASC;
```
