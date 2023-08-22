#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int totalprice;
    int a;

    cin >> totalprice;

    for (int i = 0; i < 9; i++) {
        cin >> a;
        totalprice -= a;
    }

    cout << totalprice;
}