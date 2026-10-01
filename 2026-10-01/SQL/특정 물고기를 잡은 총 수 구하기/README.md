# [SQL] 특정 물고기를 잡은 총 수 구하기

## 📌 문제 설명

낚시앱에서 사용하는 `FISH_INFO` 테이블은 잡은 물고기들의 정보를 담고 있고, `FISH_NAME_INFO` 테이블은 물고기의 이름에 대한 정보를 담고 있습니다.  
잡은 물고기 중 **'BASS'**와 **'SNAPPER'**의 총 마리 수를 출력하는 SQL문을 작성하는 문제입니다.

- **컬럼명 요구사항**: 물고기의 수를 나타내는 컬럼명은 **`FISH_COUNT`**로 지정해야 합니다.

---

## 🗂 테이블 구조

### 1. `FISH_INFO`

| Column name | Type    | Nullable | Description             |
| :---------- | :------ | :------- | :---------------------- |
| `ID`        | INTEGER | FALSE    | 잡은 물고기의 ID        |
| `FISH_TYPE` | INTEGER | FALSE    | 물고기의 종류 (숫자)    |
| `LENGTH`    | FLOAT   | TRUE     | 잡은 물고기의 길이 (cm) |
| `TIME`      | DATE    | FALSE    | 물고기를 잡은 날짜      |

### 2. `FISH_NAME_INFO`

| Column name | Type    | Nullable | Description          |
| :---------- | :------ | :------- | :------------------- |
| `FISH_TYPE` | INTEGER | FALSE    | 물고기의 종류 (숫자) |
| `FISH_NAME` | VARCHAR | FALSE    | 물고기의 이름 (문자) |

---

## 💡 정답 SQL 쿼리

```sql
SELECT COUNT(*) AS FISH_COUNT
FROM FISH_INFO FI
JOIN FISH_NAME_INFO FNI ON FI.FISH_TYPE = FNI.FISH_TYPE
WHERE FNI.FISH_NAME IN ('BASS', 'SNAPPER');
```
