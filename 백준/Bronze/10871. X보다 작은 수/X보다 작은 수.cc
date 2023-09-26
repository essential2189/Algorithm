#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>


using namespace std;

vector<int> split(string input, char d) {
    vector<int> result;
    istringstream ss(input);
    string temp;

    while (getline(ss, temp, d)) {
      result.push_back(stoi(temp));
    }

    return result;
}


int main() {
  int n, x;

  cin >> n >> x;

  string answer;
  
  while (n--) {
    int a;
    cin >> a;

    if (a < x) {
      answer += to_string(a) + ' ';
    }
  }
  
  cout << answer.substr(0, n-1);
}