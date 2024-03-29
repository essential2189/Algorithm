#include <iostream>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  string n;
  int b;

  cin >> n >> b;

  int count = 0, answer = 0;
  
  reverse(n.begin(), n.end());
  
  for (int i: n) {
    if (i >= 'A') {
      i = i + 10 - 'A';
    } else {
      i = i - '0';
    }

    answer += (int)pow(b, count) * i;
    count++;
  }

  cout << answer;
}