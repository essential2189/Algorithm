#include <iostream>
#include <string>

using namespace std;

int main() {
  int t;

  cin >> t;
  cin.ignore();

  while (t--) {
    string str;

    getline(cin, str);

    cout << str[0] << str[str.length()-1] << '\n';
  }
}