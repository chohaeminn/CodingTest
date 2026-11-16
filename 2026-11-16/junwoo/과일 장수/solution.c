#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    int x = *(const int *)a;
    int y = *(const int *)b;
    return (y > x) - (y < x);
}

// score_len은 배열 score의 길이입니다.
int solution(int k, int m, int score[], size_t score_len) {
    int answer = 0;
    int sum =0;

    qsort(score, score_len, sizeof(int), compare);

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