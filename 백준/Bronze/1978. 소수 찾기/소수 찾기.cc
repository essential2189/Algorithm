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
  string tmp;

  while (getline(ss, tmp, d)) {
    result.push_back(stoi(tmp));
  }

  return result;
}

int main() {
  int n;
  cin >> n;
  cin.ignore();

  string s;
  getline(cin, s);

  vector<int> nums(n);
  nums = split(s, ' ');

  int max_num;
  max_num = *max_element(nums.begin(), nums.end());

  nums.erase(remove(nums.begin(), nums.end(), 1), nums.end());
  for (int i = 2; i <= 1000; i++) {
    for (int j = i*2; j <= 1000; j += i) {
      nums.erase(remove(nums.begin(), nums.end(), j), nums.end());
    }
  }
  
  cout << nums.size();
}