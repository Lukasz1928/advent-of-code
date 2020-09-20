#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

void nextPassword(char* password) {
    int i = strlen(password) - 1;
    if(password[i] < 'z') {
        password[i]++;
    }
    else {
        password[i] = 'a';
        int j = i - 1;
        while(password[j] == 'z') {
            password[j] = 'a';
            j--;
        }
        password[j] = (password[j] + 1 - 'a') % 26 + 'a';
    }
}

bool hasIncreasingTriple(char* password) {
    int i;
    for(i = 0; i < strlen(password) - 2; i++) {
        if(password[i] == password[i + 1] - 1 && password[i + 1] == password[i + 2] - 1) {
            return true;
        }
    }
    return false;
}

bool hasNoAmbiguousChars(char* password) {
    int i;
    for(i = 0; i < strlen(password); i++) {
        if(password[i] == 'i' || password[i] == 'o' || password[i] == 'l') {
            return false;
        }
    }
    return true;
}

bool hasTwoDifferentPairs(char* password) {
    char letterInPair1 = -1;
    int i;
    for(i = 0; i < strlen(password) - 1; i++) {
        if(password[i] == password[i + 1]) {
            letterInPair1 = password[i];
            break;
        }
    }
    for(;i < strlen(password) - 1; i++) {
        if(password[i] != letterInPair1 && password[i] == password[i + 1]) {
            return true;
        }
    }
    return false;
}

bool isValid(char* password) {
    return hasIncreasingTriple(password) && hasNoAmbiguousChars(password) && hasTwoDifferentPairs(password);
}

char* readFile() {
    FILE* file = fopen("input", "r");
    int size = 4;
    char* data = malloc(size * sizeof(char));
    int idx = 0;
    char c;
    while((c = fgetc(file)) != EOF) {
        if(idx == size) {
            size *= 2;
            data = realloc(data, size * sizeof(char));
        }
        data[idx++] = c;
    }
    if(idx == size) {
        size += 1;
        data = realloc(data, size * sizeof(char));
    }
    data[idx] = 0;
    return data;
}

int main() {
    char* password = readFile();
    do {
        nextPassword(password);
    }
    while(!isValid(password));
    printf("%s", password);
    free(password);
    return 0;
}
