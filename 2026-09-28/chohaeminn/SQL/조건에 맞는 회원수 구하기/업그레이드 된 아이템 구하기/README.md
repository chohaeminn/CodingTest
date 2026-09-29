# 업그레이드 된 아이템 구하기

## 문제 설명

게임 아이템은 다른 아이템으로 업그레이드할 수 있다. 업그레이드 전 아이템을 `PARENT` 아이템이라고 하며, `PARENT` 아이템이 없는 아이템을 `ROOT` 아이템이라고 한다.

아이템 정보를 담은 `ITEM_INFO` 테이블과 아이템 간의 관계를 담은 `ITEM_TREE` 테이블이 주어진다.

### ITEM_INFO

| Column name | Type | Nullable | 설명 |
| --- | --- | --- | --- |
| ITEM_ID | INTEGER | FALSE | 아이템 ID |
| ITEM_NAME | VARCHAR(N) | FALSE | 아이템 이름 |
| RARITY | VARCHAR(N) | FALSE | 아이템 희귀도 |
| PRICE | INTEGER | FALSE | 아이템 가격 |

### ITEM_TREE

| Column name | Type | Nullable | 설명 |
| --- | --- | --- | --- |
| ITEM_ID | INTEGER | FALSE | 아이템 ID |
| PARENT_ITEM_ID | INTEGER | TRUE | 부모 아이템 ID |

각 아이템은 하나의 `PARENT_ITEM_ID`만 가지며, `ROOT` 아이템의 `PARENT_ITEM_ID`는 `NULL`이다.

## 문제

희귀도가 `RARE`인 아이템으로부터 **바로 다음 단계로 업그레이드할 수 있는 아이템**의 ID, 이름, 희귀도를 조회한다. 결과는 아이템 ID를 기준으로 내림차순 정렬한다.

## 풀이 방법

1. 서브쿼리에서 `RARITY = 'RARE'`인 아이템의 ID를 조회한다.
2. `ITEM_TREE.PARENT_ITEM_ID`가 조회한 ID에 포함되는 행을 찾는다.
3. `ITEM_INFO`와 `ITEM_TREE`를 `ITEM_ID`로 조인하여 자식 아이템의 정보를 가져온다.
4. 결과를 `ITEM_ID` 기준 내림차순으로 정렬한다.

## SQL

```sql
SELECT I.ITEM_ID, I.ITEM_NAME, I.RARITY
FROM ITEM_INFO I
JOIN ITEM_TREE T
    ON I.ITEM_ID = T.ITEM_ID
WHERE T.PARENT_ITEM_ID IN (
    SELECT ITEM_ID
    FROM ITEM_INFO
    WHERE RARITY = 'RARE'
)
ORDER BY I.ITEM_ID DESC;
```

## 알게 된 점

- 같은 테이블에서 조건에 맞는 ID를 먼저 찾을 때 서브쿼리를 사용할 수 있다.
- `ITEM_TREE`의 `PARENT_ITEM_ID`는 업그레이드 전 아이템을, `ITEM_ID`는 업그레이드 후 아이템을 나타낸다.
- `IN`을 사용하면 서브쿼리가 반환한 여러 ID 중 하나와 일치하는 행을 조회할 수 있다.
