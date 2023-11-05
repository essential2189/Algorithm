#include <iostream>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int dot = 2;
  int n;

  cin >> n;

  while (n--) {
    dot = dot * 2 - 1;
  }
  
  cout << dot * dot;
}