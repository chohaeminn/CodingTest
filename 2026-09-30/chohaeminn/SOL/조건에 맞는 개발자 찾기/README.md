# [SQL] 조건에 맞는 개발자 찾기 (Programmers)

## 📌 문제 설명

- **테이블 정보**:
  - `SKILLCODES`: 개발자 스킬 정보 (`NAME`, `CATEGORY`, `CODE`) - 스킬 코드는 2의 제곱수(비트 연산용)
  - `DEVELOPERS`: 개발자 정보 (`ID`, `FIRST_NAME`, `LAST_NAME`, `EMAIL`, `SKILL_CODE`)
- **요구사항**: `Python` 또는 `C#` 스킬을 가진 개발자의 `ID`, `EMAIL`, `FIRST_NAME`, `LAST_NAME` 조회
- **정렬 기준**: `ID` 기준 오름차순

---

## 💡 접근 방법 (비트 연산)

- 개발자의 `SKILL_CODE`는 여러 스킬 코드의 합(비트 OR 연산 결과)으로 이루어져 있습니다.
- 특정 스킬을 가지고 있는지 확인하기 위해 **비트 AND 연산(`&`)**을 사용합니다.
- `SKILLCODES` 테이블에서 'Python'과 'C#'의 `CODE`를 서브쿼리로 가져와 각 개발자의 `SKILL_CODE`와 비트 연산(`&`)을 수행하여 결과가 `0`보다 큰지 확인합니다.

---

## 💻 Solution

```sql
SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
FROM DEVELOPERS
WHERE SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'Python') > 0
   OR SKILL_CODE & (SELECT CODE FROM SKILLCODES WHERE NAME = 'C#') > 0
ORDER BY ID ASC;
```
