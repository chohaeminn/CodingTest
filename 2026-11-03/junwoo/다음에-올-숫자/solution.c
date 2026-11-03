#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// common_len은 배열 common의 길이입니다.
int solution(int common[], size_t common_len) {
    int sum = 0;
    int answer=0;
    int d = common[1]-common[0];
    int l = common[2]-common[1];
    
    if( d==l ){
    int d = common[1] - common[0];   
        answer = common[common_len-1]+d;
    }
    
    else{
    int r = common[1]/common[0];
    answer = common[common_len-1]*r;
    }
    return answer;
}