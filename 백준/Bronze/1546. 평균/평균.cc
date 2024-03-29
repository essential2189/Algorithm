#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cmath>
#include <set>

using namespace std;

vector<int> split(string s, char d) {
  vector<int> result;
  istringstream ss(s);
  string temp;

  while(getline(ss, temp, d)) {
    result.push_back(stoi(temp));
  }

  return result;
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int n, m;
  cin >> n;
  cin.ignore();

  string str;
  getline(cin, str);
  
  vector<int> scores = split(str, ' ');

  float sum = 0;
  float max = *max_element(scores.begin(), scores.end());

  for (int i:scores) {
    sum += i / max * 100;
  }

  cout << sum / n;
}