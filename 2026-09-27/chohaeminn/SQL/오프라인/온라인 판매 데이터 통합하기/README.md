# 프로그래머스 - 오프라인/온라인 판매 데이터 통합하기

## 문제 설명

`ONLINE_SALE`과 `OFFLINE_SALE` 테이블에서 2022년 3월의 판매 데이터를 조회하는 문제입니다.

두 테이블의 데이터를 하나로 합쳐 다음 컬럼을 출력합니다.

- 판매 날짜 (`SALES_DATE`)
- 상품 ID (`PRODUCT_ID`)
- 회원 ID (`USER_ID`)
- 판매량 (`SALES_AMOUNT`)

오프라인 판매에는 회원 정보가 없으므로 `USER_ID`를 `NULL`로 표시합니다.

결과는 다음 순서로 오름차순 정렬합니다.

1. 판매 날짜
2. 상품 ID
3. 회원 ID

## 풀이

```sql
SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE,
       PRODUCT_ID,
       USER_ID,
       SALES_AMOUNT
FROM ONLINE_SALE
WHERE SALES_DATE >= '2022-03-01'
  AND SALES_DATE < '2022-04-01'

UNION ALL

SELECT DATE_FORMAT(SALES_DATE, '%Y-%m-%d') AS SALES_DATE,
       PRODUCT_ID,
       NULL AS USER_ID,
       SALES_AMOUNT
FROM OFFLINE_SALE
WHERE SALES_DATE >= '2022-03-01'
  AND SALES_DATE < '2022-04-01'

ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC;
```

## 배운 점

### `DATE_FORMAT` 사용법

MySQL의 `DATE_FORMAT`은 날짜를 원하는 문자열 형식으로 출력할 때 사용합니다.

```sql
DATE_FORMAT(날짜, '출력 형식')
```

이번 문제에서는 다음과 같이 사용했습니다.

```sql
DATE_FORMAT(SALES_DATE, '%Y-%m-%d')
```

- `%Y`: 네 자리 연도
- `%m`: 두 자리 월
- `%d`: 두 자리 일

예를 들어 `2022-03-01 10:30:00`은 `2022-03-01`로 출력됩니다.

### `UNION ALL` 사용법

`UNION ALL`은 여러 `SELECT`문의 결과를 하나로 합칠 때 사용합니다.

```sql
SELECT 컬럼1, 컬럼2
FROM 테이블1

UNION ALL

SELECT 컬럼1, 컬럼2
FROM 테이블2;
```

합치는 두 `SELECT`문은 컬럼의 개수와 순서가 같아야 하며, 대응하는 컬럼의 자료형도 서로 호환되어야 합니다.

이번 문제에서 `OFFLINE_SALE`에는 `USER_ID`가 없으므로 다음과 같이 `NULL`을 사용해 컬럼 구조를 맞췄습니다.

```sql
NULL AS USER_ID
```

`UNION`은 중복 행을 제거하지만, `UNION ALL`은 중복 행을 제거하지 않고 모든 결과를 그대로 합칩니다. 판매 기록은 각각 보존해야 하므로 이 문제에서는 `UNION ALL`을 사용했습니다.

### 날짜 범위 조회

2022년 3월 데이터는 다음과 같이 반개방 구간으로 조회했습니다.

```sql
WHERE SALES_DATE >= '2022-03-01'
  AND SALES_DATE < '2022-04-01'
```

이 방식은 `SALES_DATE`에 시간 값이 포함되어 있어도 3월의 모든 데이터를 안전하게 조회할 수 있습니다.

### 정렬

```sql
ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC
```

앞에 작성한 컬럼부터 우선하여 정렬합니다. 판매 날짜가 같으면 상품 ID로, 상품 ID도 같으면 회원 ID로 정렬합니다.
