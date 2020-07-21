#include <stdio.h>
#include <stdlib.h>

int index_halfway_around(int length, int index) {
    int idx = index + length / 2;
    if(idx < length) {
        return idx;
    }
    return length / 2 - idx + index;
}

int main() {
    FILE* input_file = fopen("input", "r");
    int* buffer;
    int buffer_size = 16;
    buffer = (int*)malloc(buffer_size * sizeof(int));
    int buffer_idx = 0;
    int digit;
    while((digit = fgetc(input_file)) != EOF) {
        if(buffer_idx == buffer_size) {
            buffer_size *= 2;
            buffer = realloc(buffer, buffer_size * sizeof(int));
        }
        buffer[buffer_idx++] = digit - '0';
    }
    fclose(input_file);
    int input_length = buffer_idx;
    int i;
    int sum = 0;
    for(i = 0; i < input_length / 2; i++) {
        if(buffer[i] == buffer[index_halfway_around(input_length, i)]) {
            sum += buffer[i];
        }
    }
    sum *= 2;
    free(buffer);
    printf("%d", sum);
    return 0;
}
