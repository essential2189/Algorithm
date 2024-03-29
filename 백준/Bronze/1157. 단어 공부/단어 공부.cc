#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <cctype>
#include <map>

using namespace std;

bool cmp(pair<char, int> &v1, pair<char, int> &v2) {
  return v1.second > v2.second;
}

int main() {
  string s;

  getline(cin, s);

  for (char &c: s) {
    c = toupper(c);
  }

  map<char, int> m;

  for (char i: s) {
    if (m.count(i) > 0) {
      m[i] += 1;
    } else {
      m[i] = 1;
    }
  }

  vector<pair<char, int>> v;

  for (auto &s: m) {
    v.push_back(make_pair(s.first, s.second));
  }

  sort(v.begin(), v.end(), cmp);

  if(v.size() > 1) {
    if (v[0].second == v[1].second) {
      cout << '?';
      return 0;
    }
  }
  cout << v[0].first;
}
