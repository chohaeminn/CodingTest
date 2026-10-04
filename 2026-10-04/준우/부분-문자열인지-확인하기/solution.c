#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* myString, const char* pat) {
    int answer = 0;
    int size_str= strlen(myString);
    int size_pat = strlen(pat);
    int cnt = 0;
    
    for(int i =0; i<size_str-size_pat+1;i++){
        for(int j =0; j<size_pat;j++){
            
            if(tolower(myString[i+j]) != tolower(pat[j])){
                cnt = 0;
                break;
            }
            
            else{
                cnt++;
             
                }
        }
        
            if(cnt == size_pat){
                break;
            }
               
        }
    
    

    if(cnt == size_pat){
        answer =1;
    }
    else{
        answer =0;
    }

    return answer;
}