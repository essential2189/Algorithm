#include <iostream>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int n;

  cin >> n;

  if (n == 1) {
    cout << 1;
    return 0;
  }

  int min = 2, max = 7;

  int answer = 0;
  
  while (true) {
    if (n >= min && n <= max) {
      break;
    }

    answer += 1;

    max += 6 * (answer + 1);
    min += 6 * answer;
  }
  
  cout << answer + 2;
}