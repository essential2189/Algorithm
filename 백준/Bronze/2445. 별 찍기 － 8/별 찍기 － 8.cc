#include <iostream>

using namespace std;

int main() {
  int n;

  cin >> n;

  for (int i = 0; i < n; i++) {
    for (int s = 0; s <= i; s++) {
      cout << '*';
    }
    
    for (int o = n-i-1; o > 0; o--) {
      cout << ' ';
    }
    
    for (int o = n-i-1; o > 0; o--) {
      cout << ' ';
    }
    
    for (int s = 0; s <= i; s++) {
      cout << '*';
    }
    
    cout << '\n';
  }
  
  for (int i = 0; i < n; i++) {
    for (int s = n-i-1; s > 0; s--) {
      cout << '*';
    }

    for (int o = 0; o <= i; o++) {
      cout << ' ';
    }

    for (int o = 0; o <= i; o++) {
      cout << ' ';
    }

    for (int s = n-i-1; s > 0; s--) {
      cout << '*';
    }

    cout << '\n';
  }
}