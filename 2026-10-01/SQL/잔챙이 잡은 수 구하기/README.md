# [SQL] 잡은 물고기 중 길이가 10cm 이하인 물고기 수 구하기

## 📌 문제 설명

낚시앱에서 사용하는 `FISH_INFO` 테이블은 잡은 물고기들의 정보를 담고 있습니다.  
잡은 물고기의 길이가 **10cm 이하일 경우에는 `LENGTH`가 `NULL`**로 표기되며, `LENGTH`에 `NULL`만 있는 경우는 없습니다.

잡은 물고기 중 **길이가 10cm 이하인 물고기의 수**를 출력하는 SQL문을 작성하는 문제입니다.

- **컬럼명 요구사항**: 물고기의 수를 나타내는 컬럼명은 **`FISH_COUNT`**로 지정해야 합니다.

---

## 🗂 테이블 구조 (`FISH_INFO`)

| Column name | Type    | Nullable | Description             |
| :---------- | :------ | :------- | :---------------------- |
| `ID`        | INTEGER | FALSE    | 잡은 물고기의 ID        |
| `FISH_TYPE` | INTEGER | FALSE    | 물고기의 종류 (숫자)    |
| `LENGTH`    | FLOAT   | TRUE     | 잡은 물고기의 길이 (cm) |
| `TIME`      | DATE    | FALSE    | 물고기를 잡은 날짜      |

---

## 💡 정답 SQL 쿼리

```sql
SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO
WHERE LENGTH IS NULL;
```
