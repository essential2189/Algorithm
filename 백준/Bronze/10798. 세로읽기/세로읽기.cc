#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int n = 5;

  vector<vector<char>> v;

  int max = 0;
  
  while (n--) {
    string s;
    getline(cin, s);

    vector<char> vv(s.begin(), s.end());

    v.push_back(vv);

    if (vv.size() > max) {
      max = vv.size();
    }
  }

  for (int i = 0; i < max; i++) {
    for (int j = 0; j < v.size(); j++) {
      if (i < v[j].size()) {
        cout << v[j][i];
      }
    }
  }
}