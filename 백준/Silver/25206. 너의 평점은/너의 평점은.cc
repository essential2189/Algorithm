#include <iomanip>
#include <ios>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

vector<string> split(string input, char d) {
  vector<string> result;
  istringstream ss(input);
  string temp;

  while (getline(ss, temp, d)) {
    result.push_back(temp);
  }

  return result;
}

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int n = 20;
  float total = 0.0, answer = 0.0;

  map<string, float> grade = {{"A+", 4.5}, {"A0", 4.0}, {"B+", 3.5},
                            {"B0", 3.0}, {"C+", 2.5}, {"C0", 2.0},
                            {"D+", 1.5}, {"D0", 1.0}, {"F", 0.0}};

  while (n--) {
    string s;

    getline(cin, s);

    vector<string> g = split(s, ' ');

    if (g[2] != "P") {
      answer += grade[g[2]] * stof(g[1]);
      total += stof(g[1]);
    }
  }

  cout << fixed << showpoint << setprecision(6) << answer / total;
}