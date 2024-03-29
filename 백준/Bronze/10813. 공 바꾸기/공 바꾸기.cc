#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <cmath>

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

    int temp = nums[i-1];
    nums[i-1] = nums[j-1];
    nums[j-1] = temp;
  }

  for(int i: nums) {
    cout << i << ' ';
  }
}