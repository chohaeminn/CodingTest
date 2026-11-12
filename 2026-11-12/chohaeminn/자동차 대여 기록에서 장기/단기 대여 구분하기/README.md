# [프로그래머스] 자동차 대여 기록에서 장기/단기 대여 구분하기 (Lv.1)

- **문제 링크:** [프로그래머스 - 자동차 대여 기록에서 장기/단기 대여 구분하기](https://school.programmers.co.kr/learn/courses/30/lessons/151138)
- **카테고리:** String, Date
- **사용 언어:** MySQL

## 📋 문제 요약

`CAR_RENTAL_COMPANY_RENTAL_HISTORY` 테이블에서 **대여 시작일이 2022년 9월**인 기록을 조회하여, 대여 기간이 **30일 이상이면 `'장기 대여'`**, 그렇지 않으면 **`'단기 대여'`**로 표시하는 `RENT_TYPE` 컬럼을 추가해 출력합니다. (결과는 `HISTORY_ID` 기준 내림차순 정렬)

## 💻 정답 코드

```sql
SELECT
    HISTORY_ID,
    CAR_ID,
    DATE_FORMAT(START_DATE, '%Y-%m-%d') AS START_DATE,
    DATE_FORMAT(END_DATE, '%Y-%m-%d') AS END_DATE,
    CASE
        WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 30 THEN '장기 대여'
        ELSE '단기 대여'
    END AS RENT_TYPE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE START_DATE LIKE '2022-09%'
ORDER BY HISTORY_ID DESC;
```
