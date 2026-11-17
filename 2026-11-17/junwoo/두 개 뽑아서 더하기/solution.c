#include <stdio.h>
#include <stdlib.h>

int compare(const void* a, const void* b) {
    int x = *(const int*)a;
    int y = *(const int*)b;

    return (x > y) - (x < y);
}

int* solution(int numbers[], size_t numbers_len) {
    int max_size = numbers_len * (numbers_len - 1) / 2;
    int* answer = malloc(sizeof(int) * max_size);
    int count = 0;

    for (int i = 0; i < numbers_len; i++) {
        for (int j = i + 1; j < numbers_len; j++) {
            int sum = numbers[i] + numbers[j];
            int duplicate = 0;

            for (int k = 0; k < count; k++) {
                if (answer[k] == sum) {
                    duplicate = 1;
                    break;
                }
            }

            if (duplicate == 0) {
                answer[count] = sum;
                count++;
            }
        }
    }

    qsort(answer, count, sizeof(int), compare);

    return answer;
}