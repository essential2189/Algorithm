#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cmath>
#include <set>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  string str;

  getline(cin, str);
  
  int i;
  cin >> i;
  
  cout << str.at(i-1);
}