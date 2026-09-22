#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

char** solution(const char* str_list[], size_t str_list_len) {
    int idx = -1;
    char dir = 0;

    for (int i = 0; i < str_list_len; i++) {
        if (strcmp(str_list[i], "l") == 0) {
            idx = i;
            dir = 'l';
            break;
        }
        else if (strcmp(str_list[i], "r") == 0) {
            idx = i;
            dir = 'r';
            break;
        }
    }

    if (idx == -1) {
        char** answer = (char**)malloc(0);
        return answer;
    }

    if (dir == 'l') {
        char** answer = (char**)malloc(sizeof(char*) * idx);

        for (int i = 0; i < idx; i++) {
            answer[i] = (char*)malloc(strlen(str_list[i]) + 1);
            strcpy(answer[i], str_list[i]);
        }

        return answer;
    }
    else {
        int len = str_list_len - idx - 1;
        char** answer = (char**)malloc(sizeof(char*) * len);

        for (int i = 0; i < len; i++) {
            answer[i] = (char*)malloc(strlen(str_list[idx + 1 + i]) + 1);
            strcpy(answer[i], str_list[idx + 1 + i]);
        }

        return answer;
    }
}