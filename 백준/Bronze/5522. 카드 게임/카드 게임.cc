#include <iostream>

using namespace std;

int main() {
  unsigned long long answer = 0;

  int n = 5;

  while (n--) {
    unsigned long long i = 0;

    cin >> i;
    answer += i;
  }

  cout << answer;
}