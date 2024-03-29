#include <iostream>
#include <deque>
#include <string>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int n;

  cin >> n;

  deque<int> q;

  while (n--) {
    string command;

    cin >> command;

    if (command == "push_front") {
      int i;
      cin >> i;
      q.push_front(i);
    } else if (command == "push_back") {
      int i;
      cin >> i;
      q.push_back(i);
    } else if (command == "pop_front") {
      if (q.empty()) {
        cout << -1 << '\n';
      } else {
        cout << q.front() << '\n';
        q.pop_front();
      }
    } else if (command == "pop_back") {
      if (q.empty()) {
        cout << -1 << '\n';
      } else {
        cout << q.back() << '\n';
        q.pop_back();
      }
    } else if (command == "size") {
      cout << q.size()  << '\n';
    } else if (command == "empty") {
      if (q.empty()) {
        cout << 1 << '\n';
      } else {
        cout << 0 << '\n';
      }
    } else if (command == "front") {
      if (q.empty()) {
        cout << -1 << '\n';
      } else {
        cout << q.front() << '\n';
      }
    } else if (command == "back") {
      if (q.empty()) {
        cout << -1 << '\n';
      } else {
        cout << q.back() << '\n';
      }
    }
  }
}
