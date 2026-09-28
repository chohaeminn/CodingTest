조건에 맞는 회원수 구하기
조건에 맞는 회원수 구하기
문제 설명
다음은 어느 의류 쇼핑몰에 가입한 회원 정보를 담은 USER_INFO 테이블입니다. USER_INFO 테이블은 아래와 같은 구조로 되어있으며 USER_ID, GENDER, AGE, JOINED는 각각 회원 ID, 성별, 나이, 가입일을 나타냅니다.

Column name Type Nullable
USER_ID INTEGER FALSE
GENDER TINYINT(1) TRUE
AGE INTEGER TRUE
JOINED DATE FALSE
GENDER 컬럼은 비어있거나 0 또는 1의 값을 가지며 0인 경우 남자를, 1인 경우는 여자를 나타냅니다.

문제
USER_INFO 테이블에서 2021년에 가입한 회원 중 나이가 20세 이상 29세 이하인 회원이 몇 명인지 출력하는 SQL문을 작성해주세요.

## 알게 된 점

`YEAR(날짜)`를 사용하면 날짜에서 연도만 추출할 수 있다는 것을 알게 되었다.

예를 들어 `YEAR(JOINED) = 2021`처럼 작성하면 `JOINED`의 연도가 2021년인 데이터만 조회할 수 있다.
