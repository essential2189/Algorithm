#include <iostream>

using namespace std;

int main() {
  int n;

  cin >> n;

  for (int i = 0; i < n; i++) {
    if (i % 2 != 0) {
      cout << ' ';
    }
    for (int j = 0; j < n-1; j++) {
        cout << '*' << ' ';
    }
    cout << '*';

    if (i < n-1) {
      cout << '\n';
    }
  }
  
}