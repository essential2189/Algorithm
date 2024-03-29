#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

vector<int> split(string s, char d) {
  vector<int> result;
  stringstream ss(s);
  string temp;

  while(getline(ss, temp, d)) {
    result.push_back(stoi(temp));
  }

  return result;
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL) ; cout.tie(NULL);

  int n = 9;
  int max = -1;
  vector<int> max_idx(2);

  while(n--) {
    string s;

    getline(cin, s);

    vector<int> v = split(s, ' ');

    int m = *max_element(v.begin(), v.end());
    int mi = max_element(v.begin(), v.end()) - v.begin();

    if (m > max) {
      max = m;
      max_idx = {9 - n, mi + 1};
    }
  }
  
  cout << max << '\n';
  cout << max_idx[0] << ' ' << max_idx[1];
}