#include <iostream>

using namespace std;

int main() {
  int t;
  
  cin >> t;

  while (t--) {
    int s, n;
    
    cin >> s >> n;
    
    int parts = 0;
    while (n--) {
      int q, p;

      cin >> q >> p;
      
      parts += q * p;
    }
    
    cout << s + parts << '\n';
  }
}