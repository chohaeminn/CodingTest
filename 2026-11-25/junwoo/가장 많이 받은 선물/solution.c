#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// friends_len은 배열 friends의 길이입니다.
// gifts_len은 배열 gifts의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* friends[], size_t friends_len, const char* gifts[], size_t gifts_len) {
    int answer = 0;
    int record[50][50] ={0};
    int gift_index[50] = {0};
    int next_gift[50] = {0};
    
    for(int i =0; i< gifts_len; i++){
        char word1[11], word2[11];
        sscanf(gifts[i],"%10s %10s", word1, word2);
        int a,b;

        for(int j =0; j<friends_len; j++){
            if(strcmp(word1,friends[j])==0) a =j;
            if(strcmp(word2,friends[j])==0) b =j;
        }
        record[a][b]++;


    }

    for(int i =0; i<friends_len;i++){
        for(int j =0; j<friends_len; j++){
            gift_index[i] += record[i][j]-record[j][i];
        }
    }

      for(int i =0; i<friends_len;i++){
        for(int j =i+1; j<friends_len; j++){
            if(record[i][j]>record[j][i]) next_gift[i]++;
            else if(record[i][j]<record[j][i]) next_gift[j]++;
            else{
                if(gift_index[i]>gift_index[j]) next_gift[i]++;
                else if(gift_index[i]<gift_index[j]) next_gift[j]++;

            }

        }
    }
    
    for(int i =0; i<friends_len;i++){
        if(answer<next_gift[i]){
            answer=next_gift[i];
        }
    }


    return answer;
}