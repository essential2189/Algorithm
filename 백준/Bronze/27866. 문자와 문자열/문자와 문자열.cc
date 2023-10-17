#include <iostream>
#include <vector>
#include <sstream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
  string str;
  int i;

  getline(cin, str);

  cin >> i;

  vector<char> v(str.begin(), str.end());
  
  cout << v[i-1];

}