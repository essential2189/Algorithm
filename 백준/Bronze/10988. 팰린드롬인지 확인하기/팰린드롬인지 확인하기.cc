#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  string s;

  getline(cin, s);

  string s_reverse(s);
  reverse_copy(s.begin(), s.end(), s_reverse.begin());
  
  if (s == s_reverse) {
    cout << 1;
  } else {
    cout << 0;
  }
}
