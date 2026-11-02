## 사용 개념 및 문법

관계형 데이터베이스의 JOIN(조인)과 GROUP BY(그룹화), 집계 함수 COUNT()

## 해당 문법 선택 이유

서로 다른 두 테이블(`FISH_INFO`와 `FISH_NAME_INFO`)에 정보가 나뉘어 있기 때문입니다. 잡힌 물고기의 마릿수를 세려면 `FISH_INFO` 테이블이 필요하고, 물고기의 이름을 출력하려면 `FISH_NAME_INFO` 테이블이 필요합니다. 공통 컬럼인 `FISH_TYPE`을 기준으로 두 테이블을 하나로 합치는 JOIN이 필수적입니다. 이후 종류별로 묶어 마릿수를 집계하기 위해 GROUP BY와 COUNT()를 함께 사용합니다.

## 문제 해결 흐름

1. `FISH_INFO` 테이블과 `FISH_NAME_INFO` 테이블을 `FISH_TYPE` 컬럼을 기준으로 결합(JOIN)합니다.
2. 결합된 데이터를 물고기 이름(`FISH_NAME`)을 기준으로 그룹화(GROUP BY)합니다. (문제에서 전체 마릿수를 구하라고 했으므로 10cm 이하인 경우의 LENGTH NULL 값은 별도로 걸러내지 않습니다.)
3. 각 그룹별 행의 개수를 `COUNT(*)`로 세어 `FISH_COUNT`라는 별칭(Alias)을 지정합니다.
4. 집계된 마릿수(`FISH_COUNT`)를 기준으로 내림차순(`DESC`) 정렬합니다.

## 입출력 예시 및 처리 과정

- `FISH_INFO` 테이블 내 물고기 타입(FISH_TYPE): 0, 0, 0, 1, 1, 2
- `FISH_NAME_INFO` 테이블 내 이름 정보: 0(BASS), 1(SNAPPER), 2(ANCHOVY)

1. JOIN 적용 후 매칭된 데이터:
   - 0 / BASS (3건)
   - 1 / SNAPPER (2건)
   - 2 / ANCHOVY (1건)

2. GROUP BY 및 COUNT 적용:
   - BASS 그룹: 3
   - SNAPPER 그룹: 2
   - ANCHOVY 그룹: 1

3. ORDER BY DESC (내림차순) 적용 후 최종 반환:
   - 3 / BASS
   - 2 / SNAPPER
   - 1 / ANCHOVY

## 전체 코드 및 주석

```sql
-- 물고기 마릿수를 세어 FISH_COUNT로, 물고기 이름을 FISH_NAME으로 조회합니다.
SELECT COUNT(*) AS FISH_COUNT, NAME.FISH_NAME
FROM FISH_INFO INFO
-- 두 테이블의 공통 컬럼인 FISH_TYPE을 기준으로 데이터를 합칩니다.
JOIN FISH_NAME_INFO NAME
ON INFO.FISH_TYPE = NAME.FISH_TYPE
-- 물고기 이름을 기준으로 데이터를 그룹화합니다.
GROUP BY NAME.FISH_NAME
-- 잡은 수(FISH_COUNT)를 기준으로 내림차순(DESC) 정렬합니다.
ORDER BY FISH_COUNT DESC;
```
