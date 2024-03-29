#include <iostream>
#include <stack>
#include <vector>
#include <string>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int t;

  cin >> t;

  while(t--) {
    string str;

    cin >> str;

    vector<char> v(str.begin(), str.end());

    stack<char> s;
    bool isBalanced = true;

    for (char i: v) {
      if (i == '(') {
        s.push(i);
      } else {
        if (!s.empty()) {
          s.pop();
        } else {
          isBalanced = false;
          break;
        }
      }
    }

    if (isBalanced && s.empty()) {
      cout << "YES" << '\n';
    } else {
      cout << "NO" << '\n';
    }
  }
}