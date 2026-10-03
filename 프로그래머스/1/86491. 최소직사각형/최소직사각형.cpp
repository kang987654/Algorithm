#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int garo = 0, sero = 0;
    for (const auto& size : sizes) {
        garo = max(garo, max(size[0], size[1]));
        sero = max(sero, min(size[0], size[1]));
    }
    int answer = garo * sero;
    return answer;
}