# 일로 만든 아이스크림 고르기

## 문제 링크

https://school.programmers.co.kr/learn/courses/30/lessons/133026

## 문제 설명

아이스크림 가게의 상반기 주문 정보를 담은 `FIRST_HALF` 테이블과 아이스크림 성분에 대한 정보를 담은 `ICECREAM_INFO` 테이블이 있다.

**FIRST_HALF** (기본 키: `FLAVOR`)

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| SHIPMENT_ID | INT(N) | FALSE |
| FLAVOR | VARCHAR(N) | FALSE |
| TOTAL_ORDER | INT(N) | FALSE |

**ICECREAM_INFO** (기본 키: `FLAVOR`, `FLAVOR`는 `FIRST_HALF.FLAVOR`의 외래 키)

| NAME | TYPE | NULLABLE |
| --- | --- | --- |
| FLAVOR | VARCHAR(N) | FALSE |
| INGREDIENT_TYPE | VARCHAR(N) | FALSE |

`INGREDIENT_TYPE`이 `sugar_based`면 주 성분이 설탕, `fruit_based`면 주 성분이 과일인 아이스크림이다.

**문제**: 상반기 아이스크림 총주문량(`TOTAL_ORDER`)이 3,000보다 높으면서 주 성분이 과일인 아이스크림의 맛을 총주문량이 큰 순서대로 조회한다.

## 풀이

두 테이블을 `FLAVOR` 기준으로 조인한 뒤, `TOTAL_ORDER > 3000`이고 `INGREDIENT_TYPE = 'fruit_based'`인 행만 걸러 총주문량 내림차순으로 정렬한다.

- 조건이 "3,000보다 높으면서"이므로 이상(`>=`)이 아닌 초과(`>`) 비교를 사용해야 한다.
- `ORDER BY`에는 조인 결과의 `TOTAL_ORDER` 컬럼을 그대로 사용할 수 있다.
