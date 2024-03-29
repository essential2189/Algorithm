#include <cstdio>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

vector<int> split(string s, char d) {
  vector<int> result;
  istringstream ss(s);
  string temp;

  while (getline(ss, temp, d)) {
    result.push_back(stoi(temp));
  }

  return result;
}

int main() {
  int t = 2;
  int n, m;

  cin >> n >> m;
  cin.ignore();

  vector<vector<int>> vv1;
  vector<vector<int>> vv2;
  for (int i = 0; i < n; i++) {
    string s;
    getline(cin, s);

    vector<int> v = split(s, ' ');

    vv1.push_back(v);
  }

  for (int i = 0; i < n; i++) {
    string s;
    getline(cin, s);

    vector<int> v = split(s, ' ');

    vv2.push_back(v);
  }
  
  for (int i = 0; i < n; i++){
    for (int j = 0; j < m; j++){
      cout << vv1[i][j] + vv2[i][j] << ' ';
    }
    cout << '\n';
  }
}