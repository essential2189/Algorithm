#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int n, b;

  cin >> n >> b;

  string answer = "";
  int mod = 0;

  while (n >= b) {
    mod = n % b;
    n = n / b;

    if (mod >= 10) {
      mod = (char)mod + 'A' - 10;
    } else {
      mod = (char)mod + '0';
    }

    answer = (char)mod + answer;
  }
  
  if (n >= 10) {
    n = (char)n + 'A' - 10;
  } else {
    n = (char)n + '0';
  }

  cout << (char)n + answer;
}