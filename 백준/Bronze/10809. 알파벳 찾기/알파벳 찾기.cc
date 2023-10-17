#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
  string alpha = "abcdefghijklmnopqrstuvwxyz";
  string s;

  getline(cin, s);

  for (char a: alpha) {
    cout << (int)s.find(a) << ' ';
  }
}