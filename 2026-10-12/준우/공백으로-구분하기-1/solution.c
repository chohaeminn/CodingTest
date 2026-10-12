#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char** solution(const char* my_string) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int len = strlen(my_string);
    int cnt=0;

    for(int i =0;i<len;i++){
        if(isspace(my_string[i])){
            cnt++;
        }
    }

    char** answer = (char**)malloc(sizeof(char*)*(cnt+1));

    char* temp =  (char*)malloc(sizeof(char)*(len+1));
    
    for(int i =0; i<len;i++){
        temp[i] = my_string[i];
        }
    temp[len] = '\0';
    
    char *tok = strtok(temp, " ");
    int tok_len = strlen(tok);

    answer[0] = (char*)malloc(sizeof(char)*(tok_len+1));

    strcpy(answer[0],tok); 
    int i =1;
    
    while((tok = strtok(NULL, " ")) != NULL){
            int toks_len = strlen(tok);
            answer[i] = (char*)malloc(sizeof(char)*(toks_len+1)); 
            strcpy(answer[i],tok);
            i++;
    }

    
    return answer;
}