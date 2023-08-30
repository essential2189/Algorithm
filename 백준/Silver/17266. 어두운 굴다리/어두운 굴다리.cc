#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <cmath>

using namespace std;

int main() {
    int n, m;

    cin >> n >> m;

    vector<int> lights(m);
    for (int i = 0; i < m; i++) cin >> lights[i];

    double max_count = 0;


    
    max_count = max(lights.front(), n - lights.back());

    for (int i = 0; i < lights.size()-1; i++) {
        int tmp = lights[i+1] - lights[i];

        max_count = max(max_count, ceil(tmp / 2.0));
    }

    cout << (int)max_count;
}