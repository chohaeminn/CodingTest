# 3월에 태어난 여성 회원 목록 출력하기

- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131120
- 분류: `SELECT`, `WHERE`, `ORDER BY`

## 문제 설명

`MEMBER_PROFILE` 테이블에서 생일이 3월인 여성 회원의 정보를 조회하는 문제입니다.

다음 항목을 출력합니다.

- 회원 ID
- 회원 이름
- 성별
- 생년월일

전화번호가 없는 회원은 결과에서 제외하고, 회원 ID를 기준으로 오름차순 정렬합니다.

## 풀이 설명

1. `MONTH(DATE_OF_BIRTH) = 3` 조건으로 생일이 3월인 회원을 찾습니다.
2. `GENDER = 'W'` 조건으로 여성 회원만 조회합니다.
3. `TLNO IS NOT NULL` 조건으로 전화번호가 등록된 회원만 선택합니다.
4. `DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d')`를 사용하여 생년월일을 문제에서 요구한 형식으로 출력합니다.
5. `MEMBER_ID ASC`로 회원 ID를 오름차순 정렬합니다.

## 주의사항

NULL 값은 `= NULL`이 아니라 `IS NULL` 또는 `IS NOT NULL`로 비교해야 합니다. 또한 `DATE_OF_BIRTH`의 출력 형식이 예시와 일치해야 합니다.

## 풀이 코드

풀이 코드는 [`solution.sql`](./solution.sql)에 있습니다.
