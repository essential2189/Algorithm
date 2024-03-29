#include <iostream>
#include <deque>
#include <cmath>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  int n;
  cin >> n;

  deque<int> balloon;
  deque<int> queue;

  for (int i = 0; i < n; i++) {
    int a;
    cin >> a;
    queue.push_back(a);
  }
  
  for (int i = 1; i <= n; i++) {
    balloon.push_back(i);
  }

  cout << balloon.front() << ' ';
  balloon.pop_front();

  while (queue.size() > 1) {
    int num = queue.front();
    queue.pop_front();

    if (num > 0) {
      num -= 1;
      for (int i = 0; i < num; i++) {
        queue.push_back(queue.front());
        queue.pop_front();

        balloon.push_back(balloon.front());
        balloon.pop_front();
      }
    } else {
      num = abs(num);
      for (int i = 0; i < num; i++) {
        queue.push_front(queue.back());
        queue.pop_back();

        balloon.push_front(balloon.back());
        balloon.pop_back();
      }
    }

    cout << balloon.front() << ' ';
    balloon.pop_front();
  }
}
