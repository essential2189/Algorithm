#include <iostream>

using namespace std;

int main() {
  int n;

  cin >> n;

  for (int i = 0; i < n; i++) {
    for (int s = 0; s < i; s++) {
      cout << ' ';
    }
    
    for (int o = n-i; o > 0; o--) {
      cout << '*';
    }
    
    for (int o = n-i-1; o > 0; o--) {
      cout << '*';
    }
    
    cout << '\n';
  }
  
  for (int i = 0; i < n-1; i++) {
    for (int s = n-i-2; s > 0; s--) {
      cout << ' ';
    }

    for (int o = 0; o <= i+1; o++) {
      cout << '*';
    }

    for (int o = 0; o <= i; o++) {
      cout << '*';
    }

    cout << '\n';
  }
}