// Example program
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void print(std::vector<string> const &input) {
    for (int i = 0; i< input.size(); i++) {
        std::cout << input.at(i) << ' ';
    }
}

int main()
{
    int n, p;
    cin >> n;
    
    while(n--){
        cin >> p;
        int price;
        string name;
        
        int max = 0;
        string answer;
        
        while(p--) {
            cin >> price >> name;
            if (price > max) {
                max = price;
                answer = name;
            }
        }
        cout << answer << endl;
    }
}
