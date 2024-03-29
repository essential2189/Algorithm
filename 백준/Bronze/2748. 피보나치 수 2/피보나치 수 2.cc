#include <iostream>
#include <algorithm>

using namespace std;
long long dp[100] = {0,1,};
long long fibonacci(int n) {
    if (n == 0 || n == 1) {
        return dp[n];
    }
    
    if (dp[n] == 0) {
        dp[n] = fibonacci(n-1) + fibonacci(n-2);
    }

    return dp[n];
}

int main() {
    int n;

    cin >> n;

    cout << fibonacci(n);
}