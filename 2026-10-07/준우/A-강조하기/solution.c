#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* myString) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
       int num = strlen(myString);
    char* answer = (char*)malloc(sizeof(char)*(num+1));
 

    for(int i =0; i<num; i++){
        if(myString[i] =='a'){
            answer[i] = 'A'; 
        }

        else if(myString[i] == 'A'){
            answer[i] = myString[i];
        }

        else{
            answer[i] = tolower(myString[i]);
        }
    }

    answer[num] = '\0';
    return answer;
}