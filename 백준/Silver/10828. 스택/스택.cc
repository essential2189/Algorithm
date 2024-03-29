#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int n;

  cin >> n;

  stack<int> stack;

  while (n--) {
    string command;
    int push;

    cin >> command;

    if (command == "push") {
      cin >> push;
      stack.push(push);
    } else if (command == "pop") {
      if (!stack.empty()) {
        cout << stack.top() << '\n';
        stack.pop();
      } else {
        cout << -1 << '\n';
      }
    } else if (command == "size") {
      cout << stack.size() << '\n';
    } else if (command == "empty") {
      cout << stack.empty() << '\n';
    } else if (command == "top") {
      if (!stack.empty()) {
        cout << stack.top() << '\n';
      } else {
        cout << -1 << '\n';
      }
    }
  }
}