#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  int n;

  cin >> n;
  cin.ignore();

  string nums;

  getline(cin, nums);

  vector<char> v(nums.begin(), nums.end());

  int answer = 0;
  for(char i: v) {
    answer += i - '0';
  }
  
  cout << answer;
}