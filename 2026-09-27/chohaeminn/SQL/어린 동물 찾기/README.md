# 프로그래머스 - 어린 동물 찾기

## 문제 설명

`ANIMAL_INS` 테이블에는 동물 보호소에 들어온 동물의 정보가 저장되어 있습니다.
이 테이블에서 보호 시작 시 상태인 `INTAKE_CONDITION`이 `Aged`가 아닌 동물의 아이디와 이름을 조회하는 문제입니다.

결과는 동물 아이디인 `ANIMAL_ID`를 기준으로 오름차순 정렬합니다.

## 테이블 구조

| 컬럼명 | 타입 | NULL 허용 | 설명 |
| --- | --- | --- | --- |
| `ANIMAL_ID` | `VARCHAR` | FALSE | 동물 아이디 |
| `ANIMAL_TYPE` | `VARCHAR` | FALSE | 생물 종 |
| `DATETIME` | `DATETIME` | FALSE | 보호 시작일 |
| `INTAKE_CONDITION` | `VARCHAR` | FALSE | 보호 시작 시 상태 |
| `NAME` | `VARCHAR` | TRUE | 동물 이름 |
| `SEX_UPON_INTAKE` | `VARCHAR` | FALSE | 성별 및 중성화 여부 |

## 풀이

```sql
SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE INTAKE_CONDITION != 'Aged'
ORDER BY ANIMAL_ID;
```

## 풀이 설명

### 조회할 컬럼 선택

```sql
SELECT ANIMAL_ID, NAME
```

문제에서 요구하는 동물 아이디와 이름만 조회합니다.

### 어린 동물만 조회

```sql
WHERE INTAKE_CONDITION != 'Aged'
```

`!=`는 두 값이 서로 같지 않은지 비교하는 연산자입니다.
따라서 `INTAKE_CONDITION`이 `'Aged'`가 아닌 행만 선택합니다.

표준 SQL의 같지 않음 연산자인 `<>`를 사용해도 같은 의미입니다.

```sql
WHERE INTAKE_CONDITION <> 'Aged'
```

### 아이디 순으로 정렬

```sql
ORDER BY ANIMAL_ID;
```

정렬 방향을 생략하면 기본값인 오름차순(`ASC`)으로 정렬됩니다.
다음 코드와 같은 의미입니다.

```sql
ORDER BY ANIMAL_ID ASC;
```

## 배운 점

문자열이 특정 값과 다른지 비교할 때는 `IS NOT`이 아니라 `!=` 또는 `<>`를 사용해야 한다는 것을 배웠습니다.

```sql
-- 잘못된 문자열 비교
WHERE INTAKE_CONDITION IS NOT 'Aged'

-- 올바른 문자열 비교
WHERE INTAKE_CONDITION != 'Aged'
```

`IS NOT`은 일반적으로 `NULL` 여부를 검사할 때 사용합니다.

```sql
WHERE NAME IS NOT NULL
```

정리하면 다음과 같습니다.

| 목적 | 사용 방법 |
| --- | --- |
| 값이 `'Aged'`와 다름 | `!= 'Aged'` 또는 `<> 'Aged'` |
| 값이 `NULL`이 아님 | `IS NOT NULL` |
