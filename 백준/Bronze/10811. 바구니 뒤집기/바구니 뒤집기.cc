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

  int n, m;
  cin >> n >> m;

  vector<int> nums;

  for(int i = 1; i <= n; i++) {
    nums.push_back(i);
  }

  while(m--) {
    int i, j;

    cin >> i >> j;

    reverse(nums.begin()+i-1, nums.begin()+j);
  }
  for(int i: nums) {
    cout << i << ' ';
  }
}