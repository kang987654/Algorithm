#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> p1 = {1, 2, 3, 4, 5};
    vector<int> p2 = {2, 1, 2, 3, 2, 4, 2, 5};
    vector<int> p3 = {3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
    vector<int> score = {0, 0, 0, 0};
    
    for (int i = 0; i < answers.size(); i++) {
        if (answers[i] == p1[i % p1.size()]) {
            score[1]++;
        }
        if (answers[i] == p2[i % p2.size()]) {
            score[2]++;
        }
        if (answers[i] == p3[i % p3.size()]) {
            score[3]++;
        }    
    }
    
    int max_score = *max_element(score.begin(), score.end());
    vector<int> answer;
    for (int i = 1; i < 4; i++) {
        if (score[i] == max_score) {
            answer.push_back(i);
        }
    }
    return answer;
}