#include <iostream>

using namespace std;

int main() {
  int n;
  
  cin >> n;
  
  for (int i = 0; i < n; i++) {
    for (int o = 0; o < i; o++) {
      cout << ' ';
    }
    
    for (int k = n-i; k > 0; k--) {
      cout << '*';
    }
    
    for (int k = n-i-1; k > 0; k--) {
      cout << '*';
    }
    
    cout << '\n';
  }
}