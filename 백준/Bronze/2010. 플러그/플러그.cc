#include <iostream>

using namespace std;

int main() {
  int n;

  cin >> n;

  int answer = 1;
  while (n--) {
    int i;
    
    cin >> i;
    
    answer += i - 1;
  }
  
  cout << answer;
}