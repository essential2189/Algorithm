#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

vector<int> split(string input, char d) {
    vector<int> result;
    istringstream ss(input);
    string temp;

    while (getline(ss, temp, d)) {
        result.push_back(stoi(temp));
    }

    return result;
}

int main()
{
    string firstTime, secondTime;

    cin >> firstTime;
    cin >> secondTime;

    vector<int> timeArray1 = split(firstTime, ':');
    vector<int> timeArray2 = split(secondTime, ':');

    int time1 = timeArray1[0] * 60 * 60 + timeArray1[1] * 60 + timeArray1[2];
    int time2 = timeArray2[0] * 60 * 60 + timeArray2[1] * 60 + timeArray2[2];

    if (time1 > time2) time2 += 3600 * 24;
    int s = time2 - time1;

    int hour = s / 3600;
    int minute = (s % 3600) / 60;
    int second = s % 60;

    string answer;
    if (hour == 24) hour = 0;
    if (hour < 10) answer += '0';
    answer += to_string(hour);

    answer += ':';

    if (minute < 10) answer += '0';
    answer += to_string(minute);

    answer += ':';

    if (second < 10) answer += '0';
    answer += to_string(second);

    cout << answer;
}
