#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cmath>

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

  int n, v;
  string str;

  cin >> n;
  cin.ignore();
  getline(cin, str);
  
  vector<int> nums = split(str, ' ');
  
  cout << *min_element(nums.begin(), nums.end()) << ' ' << *max_element(nums.begin(), nums.end());
}