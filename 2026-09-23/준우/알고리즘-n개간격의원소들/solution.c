#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int* solution(int num_list[], size_t num_list_len, int n) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int cnt =1;
    int num1=0;
    
    while(cnt<=num_list_len){
        num1++;
        cnt+=n;
    }
    
    int* answer = (int*)malloc(sizeof(int)*num1);

    int num2=0;
    int i =0;

    while(i<num1){

        answer[i] = num_list[num2];
        num2 +=n;
        i++;


    }
    
    

    
    
    return answer;
}