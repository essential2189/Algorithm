#include <iostream>
#include <string>

using namespace std;

int main() {
  int t;

  cin >> t;


  while (t--) {
    int r;
    string s;

    cin >> r >> s;

    string answer = "";

    for (char c: s) {
      for(int a = 0; a < r; a++){
        answer += c;
      }
    }

    cout << answer << '\n';
  }
}