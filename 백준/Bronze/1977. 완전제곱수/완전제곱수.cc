// Example program
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main()
{
  int M, N;
  cin >> M >> N;
  
  int sum = 0;
  int min = 99999999;
  bool flag = false;
  for (int i = 1; pow(i, 2) <= N; i++) {
      int power = pow(i, 2);
      if (M <= power && power <= N) {
          if (power < min) {
              min = power;
          }
          sum += power;
          flag = true;
      }
  }
  
  if (flag) {
      cout << sum << "\n";
      cout << min << "\n";
  } else {
      cout << -1;
  }
}