#include <iostream>

using namespace std;

int main() {
  int t;

  cin >> t;

  while (t--) {
    int v, e;
    
    cin >> v >> e;
    
    // v - e + {x} = 2
    cout << 2 - v + e << '\n';
  }
}