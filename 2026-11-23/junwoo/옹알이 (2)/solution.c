#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>


// babbling_len은 배열 babbling의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* babbling[], size_t babbling_len) {
    int answer = 0;
    for(int i =0; i< babbling_len; i++){
        int j =0;
        int prev =-1;
        int vaild =0;
        while (j < strlen(babbling[i])) {
            
                if (strncmp(babbling[i] + j, "aya", 3) == 0 && prev !=0) {
                    j += 3;
                    prev =0;
                }
                else if (strncmp(babbling[i] + j, "ye", 2) == 0 && prev != 1) {
                    j += 2;
                    prev =1;
                }
                else if (strncmp(babbling[i]+j,"woo",3)==0 && prev != 2) {
                    j += 3;
                    prev =2;
                }
                else if (strncmp(babbling[i] + j, "ma", 2)==0 && prev !=3 ) {
                    j += 2;
                    prev =3;
                }

                else {
                    vaild = 100;
                    break;
                }

            }
        if(vaild != 100){
            answer++;
        }

        }

    return answer;
}