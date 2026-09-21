#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int numer1, int denom1, int numer2, int denom2) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*2);
    
    int n =1;
    
    while(1){
        if(n % denom1 == 0 && n % denom2 ==0){
            break;
        }
        n++;
    }

    
    int a = n/ denom1;
    int b = n/ denom2;
    
    
    numer1 *=a;
    numer2 *=b;
    int numer_sum = numer1+numer2;

    int m;
    if(numer_sum <= n){
        m=numer_sum;
        
    }
    else{
        m=n;
    }
    
    while(1){
        if(numer_sum % m ==0 && n % m ==0){
            break;
        }
        m--;
    }
    
    numer_sum /= m;
    n /= m;
    
    answer[0] = numer_sum;
    answer[1] = n;
  
    
    
    return answer;
}