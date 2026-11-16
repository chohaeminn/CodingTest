#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// score_len은 배열 score의 길이입니다.
int solution(int k, int m, int score[], size_t score_len) {
    int answer = 0;
    int sum =0;
    for(int i =0; i<score_len-1;i++){
        for(int j =0; j< score_len-i-1; j++){
            if(score[j]<score[j+1]){
                int temp = score[j];
                score[j] = score[j+1];
                score[j+1] =temp;
            }
        }
    }

    int box = score_len/m;
    int sell = box*m;
    for(int i =0; i<sell; i++){
        if((i+1)%m==0){
            sum += score[i]*m;
        }
    }

    answer = sum;





    return answer;
}