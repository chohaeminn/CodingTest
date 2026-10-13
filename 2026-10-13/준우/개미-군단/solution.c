#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int hp) {
    int answer = 0;
    int gen_ant = hp/5;
    hp -= gen_ant*5;
    int sol_ant = hp/3;
    hp -= sol_ant*3;
    int nor_ant = hp;
    
    answer = gen_ant + sol_ant + nor_ant;

    return answer;
}