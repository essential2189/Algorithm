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

  set<int> nums;

  int n = 10;
  while(n--) {
    int i;
    cin >> i;
    nums.insert(i % 42);
  }
  
  cout << nums.size();
}