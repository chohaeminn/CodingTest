# Python 개발자 찾기

- 문제: [프로그래머스 - Python 개발자 찾기](https://school.programmers.co.kr/learn/courses/30/lessons/276013)
- 분류: SELECT
- 사용 언어: MySQL

## 문제 요약

`DEVELOPER_INFOS` 테이블에서 Python 스킬을 가진 개발자를 찾아 다음 정보를 조회한다.

- `ID`
- `EMAIL`
- `FIRST_NAME`
- `LAST_NAME`

결과는 `ID`를 기준으로 오름차순 정렬한다.

## 풀이

개발자의 스킬은 `SKILL_1`, `SKILL_2`, `SKILL_3` 열에 나누어 저장되어 있다.
따라서 세 열 중 하나라도 `'Python'`인 행을 `WHERE`절에서 찾으면 된다.

```sql
WHERE SKILL_1 = 'Python'
   OR SKILL_2 = 'Python'
   OR SKILL_3 = 'Python'
```

여러 조건을 `OR`로 연결했으므로 하나 이상의 열에 Python이 저장된 개발자가 조회된다.

마지막으로 `ORDER BY ID ASC`를 사용해 `ID`를 오름차순으로 정렬한다.

## 풀이 코드

```sql
SELECT ID,
       EMAIL,
       FIRST_NAME,
       LAST_NAME
FROM DEVELOPER_INFOS
WHERE SKILL_1 = 'Python'
   OR SKILL_2 = 'Python'
   OR SKILL_3 = 'Python'
ORDER BY ID ASC;
```
