#include <iostream>
#include <fstream>
#include <algorithm>

int main() {
    std::ifstream file("input");
    std::vector<std::string> lines;
    std::string line;
    while(getline(file, line)) {
        lines.push_back(line);
    }
    file.close();
    int locX = 1;
    int locY = 1;
    std::vector<int> digits;
    for(auto line : lines) {
        for(auto dir : line) {
            if(dir == 'U') {
                locY = std::max(locY - 1, 0);
            }
            else if(dir == 'D') {
                locY = std::min(locY + 1, 2);
            }
            else if(dir == 'L') {
                locX = std::max(locX - 1, 0);
            }
            else if(dir == 'R') {
                locX = std::min(locX + 1, 2);
            }
        }
        digits.push_back(3 * locY + locX + 1);
    }
    std::string result = "";
    for(auto d : digits) {
        result += (char)(d + '0');
    }
    std::cout << result << std::endl;
    return 0;
}
