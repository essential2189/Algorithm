#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int a, b;

    cin >> a >> b;

    int i, j;
    int maxNum = max(a, b);
    int minNum = min(a, b);

    for (i = maxNum; i >= 2; i--) {
        if (a % i == 0 && b % i == 0) {
            break;
        }
    }

    for (j = minNum; j <= a * b; j += i) {
        if (j % a == 0 && j % b == 0) {
            break;
        }
    }

    cout << i << '\n' << j << '\n';
}