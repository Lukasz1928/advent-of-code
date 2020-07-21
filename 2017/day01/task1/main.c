#include <stdio.h>

int main() {
    FILE* input_file = fopen("input", "r");
    int digit, previous_digit, first_digit;
    int sum = 0;
    previous_digit = first_digit = fgetc(input_file);
    while((digit = fgetc(input_file)) != EOF) {
        if(previous_digit == digit) {
            sum += previous_digit - '0';
        }
        previous_digit = digit;
    }
    if(previous_digit == first_digit) {
        sum += previous_digit - '0';
    }
	fclose(input_file);
    printf("%d\n", sum);
    return 0;
}
