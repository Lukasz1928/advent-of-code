#include <iostream>
#include <fstream>
#include <algorithm>

int main() {
    char digits[5][5] = {{0, 0, '1', 0, 0}, {0, '2', '3', '4', 0}, {'5', '6', '7', '8', '9'}, {0, 'A', 'B', 'C', 0}, {0, 0, 'D', 0, 0}};
    std::ifstream file("input");
    std::vector<std::string> lines;
    std::string line;
    while(getline(file, line)) {
        lines.push_back(line);
    }
    file.close();
    int locX = 0;
    int locY = 2;
    int prevX, prevY;
    std::string number;
    for(auto line : lines) {
        for(auto dir : line) {
            prevX = locX;
            prevY = locY;
            if(dir == 'U') {
                locY = std::max(locY - 1, 0);
            }
            else if(dir == 'D') {
                locY = std::min(locY + 1, 4);
            }
            else if(dir == 'L') {
                locX = std::max(locX - 1, 0);
            }
            else if(dir == 'R') {
                locX = std::min(locX + 1, 4);
            }
            if(digits[locY][locX] == 0) {
                locX = prevX;
                locY = prevY;
            }
        }
        number += digits[locY][locX];
    }
    std::cout << number << std::endl;
    return 0;
}
