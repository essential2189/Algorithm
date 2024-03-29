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

  vector<int> bag(n);

  while(m--) {
    int i, j, k;
    cin >> i >> j >> k;

    for (int t = i-1; t <= j-1; t++) {
      bag[t] = k;
    }
  }
  
  for (int i: bag) {
    cout << i << ' ';
  }
}