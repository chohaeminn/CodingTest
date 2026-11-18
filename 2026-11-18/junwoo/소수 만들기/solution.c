#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// nums_len은 배열 nums의 길이입니다.
int solution(int nums[], size_t nums_len) {
    int answer = 0;
    for(int i =0; i<nums_len; i++){
        for(int j=i+1; j<nums_len; j++){
            for(int k=j+1; k<nums_len; k++){
                int sum = nums[i]+nums[j]+nums[k];
                int isPrime =1;
                for(int p = 2; p<sum;p++){
                    if(sum%p==0){
                        isPrime =0;
                        break;
                    }
                }
                if(isPrime ==1){
                    answer++;
                }
            }
        }
    }
    
    return answer;
}