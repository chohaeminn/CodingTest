# 1로 만들기

## 문제 설명
정수가 담긴 리스트 `num_list`가 주어집니다.

`num_list`의 모든 원소를 1로 만들기 위해 다음과 같은 연산을 반복합니다.

- 값이 짝수라면 2로 나눕니다.
- 값이 홀수라면 1을 뺀 뒤 2로 나눕니다.

모든 원소를 1로 만들기 위해 필요한 연산 횟수의 합을 반환합니다.

## 풀이 방법
1. `for`문을 이용해 `num_list`의 원소를 하나씩 확인한다.
2. 각 원소가 1이 될 때까지 `while`문을 반복한다.
3. 현재 값이 짝수이면 2로 나눈다.
4. 홀수이면 1을 뺀 후 2로 나눈다.
5. 연산을 수행할 때마다 `answer`를 1씩 증가시킨다.
6. 모든 원소에 대한 연산 횟수를 합산하여 반환한다.

## 코드

```c
#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int num_list[], size_t num_list_len) {
    int answer = 0;

    for(int i = 0; i < num_list_len; i++) {
        while(num_list[i] != 1) {
            if(num_list[i] % 2 == 0) {
                num_list[i] /= 2;
                answer++;
            }
            else {
                num_list[i] = (num_list[i] - 1) / 2;
                answer++;
            }
        }
    }

    return answer;
}