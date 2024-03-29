#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int t;

  cin >> t;

  // 0.25 0.1 0.05 0.01
  
  while (t--) {
    int c;

    cin >> c;

    int q = c / 25;
    c -= 25 * q;
    int d = (c % 25) / 10;
    c -= 10 * d;
    int n = (c % 10) / 5;
    c -= 5 * n;
    int p = (c % 5);

    cout << q << ' ' << d << ' ' << n << ' ' << p << '\n';
  }
}