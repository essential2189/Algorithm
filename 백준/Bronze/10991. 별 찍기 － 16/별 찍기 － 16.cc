#include <iostream>

using namespace std;

int main() {
  int n;

  cin >> n;

  for (int i = n; i > 0; i--) {
    for (int o = i; o > 1; o--) {
      cout << ' ';
    }

    for (int s = 0; s <= n-i-1; s++) {
      cout << "* ";
    }
    
    cout << "*\n";
  }
}