#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int solution(int num_list[], size_t num_list_len) {
        
    int answer = 0;
    int num_even=0;
    int num_odd=0;
    
    for(int i =0; i<num_list_len; i+=2)
    {
        num_even +=num_list[i];
    }
    
    for(int i =1; i<num_list_len; i+=2){
        num_odd += num_list[i];
    }

    if(num_even>num_odd){
        answer = num_even;
    }

    else{
        answer = num_odd;
    }
    
    return answer;
}