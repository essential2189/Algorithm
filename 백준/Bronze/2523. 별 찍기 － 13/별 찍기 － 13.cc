#include <iostream>

using namespace std;

int main() {
  int n;
  
  cin >> n;
  
  for (int i = 0; i < n; i++) {
    for (int k = 0; k <= i; k++) {
      cout << '*';
    }
    
    cout << '\n';
  }
  
  for (int i = 0; i < n; i++) {
    for (int k = n-i-1; k > 0; k--) {
      cout << '*';
    }

    cout << '\n';
  }
}