#include <iostream>

using namespace std;

int main() {
  int n;
  
  cin >> n;
  
  for (int i = 0; i < n; i++) {
    for (int k = n-i-1; k > 0; k--) {
      cout << ' ';
    }
    
    for (int s = 0; s <= i; s++){
      cout << '*';
    }
    
    for (int s = 0; s <= i-1; s++){
      cout << '*';
    }
    
    cout << '\n';
  }
}