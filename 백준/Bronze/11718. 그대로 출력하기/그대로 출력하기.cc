#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  int i = 100;
  while (i--) {
    string s;

    getline(cin, s);

    cout << s << '\n';
  }
}
