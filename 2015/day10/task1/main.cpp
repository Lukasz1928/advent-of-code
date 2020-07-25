#include <iostream>
#include <fstream>
#include <sstream>

std::string int2str(int i) {
    std::stringstream ss;
    ss << i;
    std::string str = ss.str();
    return str;
}

std::string readInput() {
    std::ifstream file("input");
    std::string line;
    getline(file, line);
    file.close();
    return line;
}

std::string nextValue(std::string str) {
    std::string result = "";
    char c;
    int cnt;
    int i = 0;
    while(i < str.length()) {
        c = str[i];
        cnt = 0;
        while(str[i] == c) {
            cnt++;
            i++;
        }
        result += int2str(cnt) + c;
    }
    return result;
}

int main() {
    std::string value = readInput();
    for(int i = 0; i < 40; i++) {
        value = nextValue(value);
    }
    int result = value.length();
    std::cout << result;
    return 0;
}
