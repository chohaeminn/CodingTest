# 물고기 종류 별 대어 찾기 (Find the Largest Fish by Species)

프로그래머스 SQL 문제인 '물고기 종류 별 대어 찾기'의 풀이 및 핵심 개념 설명입니다.

---

## 문제 핵심 요약

- **목표:** 물고기 종류별로 가장 큰 물고기의 ID, 이름(FISH_NAME), 길이(LENGTH)를 출력하기
- **조건:**
  - 물고기 ID 기준 오름차순 정렬 (`ORDER BY ID ASC`)
  - 종류별 가장 큰 물고기는 1마리만 존재함

---

## 정답 SQL 코드

```sql
SELECT INFO.ID, NAME.FISH_NAME, INFO.LENGTH
FROM FISH_INFO INFO
JOIN FISH_NAME_INFO NAME
  ON INFO.FISH_TYPE = NAME.FISH_TYPE
WHERE (INFO.FISH_TYPE, INFO.LENGTH) IN (
    SELECT FISH_TYPE, MAX(LENGTH)
    FROM FISH_INFO
    GROUP BY FISH_TYPE
)
ORDER BY INFO.ID ASC;
```
