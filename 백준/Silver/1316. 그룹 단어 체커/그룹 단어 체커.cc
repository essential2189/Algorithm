#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int n, answer = 0;

  cin >> n;
  cin.ignore();

  while(n--) {
    string s;

    getline(cin, s);

    vector<char> v(s.begin()+1, s.end());
    map<char, int> m = {{s[0], 1}};
    char pre = s[0];
    bool flag = true;

    for (char i: v) {
      if (m.count(i) == 0) {
        m[i] = 1;
      } else {
        if (pre != i) {
          flag = false;
          break;
        }
      }
      pre = i;
    }

    if (flag) {
      answer += 1;
    }
  }
  
  cout << answer;
}