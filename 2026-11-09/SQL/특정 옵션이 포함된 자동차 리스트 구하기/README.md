# [프로그래머스] 네비게이션 옵션이 포함된 자동차 리스트 구하기 - SQL (MySQL / Oracle)

## 📌 문제 설명

`CAR_RENTAL_COMPANY_CAR` 테이블에서 **'네비게이션'** 옵션이 포함된 자동차 리스트를 출력하는 SQL문을 작성해 주세요.
결과는 **자동차 ID(`CAR_ID`)를 기준으로 내림차순** 정렬해야 합니다.

### 테이블 구조 (`CAR_RENTAL_COMPANY_CAR`)

| Column name | Type         | Nullable | 설명                                                    |
| :---------- | :----------- | :------- | :------------------------------------------------------ |
| `CAR_ID`    | INTEGER      | FALSE    | 자동차 ID                                               |
| `CAR_TYPE`  | VARCHAR(255) | FALSE    | 자동차 종류 ('세단', 'SUV', '승합차', '트럭', '리무진') |
| `DAILY_FEE` | INTEGER      | FALSE    | 일일 대여 요금(원)                                      |
| `OPTIONS`   | VARCHAR(255) | FALSE    | 자동차 옵션 리스트 (콤마로 구분된 문자열)               |

---

## 💡 풀이 핵심 아이디어

1. **부분 문자열 검색 (`LIKE` 연산자):**
   - `OPTIONS` 컬럼은 `'스마트키,네비게이션,열선시트'` 처럼 여러 옵션이 하나의 문자열로 결합되어 있습니다.
   - 문자열 내에 `'네비게이션'`이 위치에 상관없이 포함되어 있는지를 확인하기 위해 와일드카드 `%`를 사용해 `OPTIONS LIKE '%네비게이션%'` 조건을 적용합니다.

2. **내림차순 정렬 (`ORDER BY ... DESC`):**
   - 문제 요구사항에 따라 `CAR_ID`를 기준으로 내림차순(`DESC`) 정렬합니다.

---

## 💻 정답 코드 (`solution.sql`)

```sql
SELECT CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS
FROM CAR_RENTAL_COMPANY_CAR
WHERE OPTIONS LIKE '%네비게이션%'
ORDER BY CAR_ID DESC;
```
