#include <iostream>

using namespace std;

int main() {
  int n;

  cin >> n;

  int answer = 1;
  
  for (int i = n; i > 0; i--) {
    answer *= i;
  }
  
  cout << answer;
}