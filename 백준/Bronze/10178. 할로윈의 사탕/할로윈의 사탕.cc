#include <iostream>

using namespace std;

int main() {
  int t;

  cin >> t;

  while (t--) {
    int c, v;

    cin >> c >> v;

    int brother = c / v;
    int father = c % v;

    cout << "You get " << brother << " piece(s) and your dad gets " << father << " piece(s).\n";
  }
}