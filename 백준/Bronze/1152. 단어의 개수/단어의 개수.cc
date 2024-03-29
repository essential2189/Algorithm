#include <iostream>
#include <sstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

vector<string> split(string s, char d) {
  vector<string> result;
  istringstream ss(s);
  string temp;

  while(getline(ss, temp, d)) {
    result.push_back(temp);
  }

  return result;
}

inline string& ltrim(string& s, const char* t = " \t\n\r\f\v") {
  s.erase(0, s.find_first_not_of(t));
  return s;
}

inline string& rtrim(string& s, const char* t = " \t\n\r\f\v") {
  s.erase(s.find_last_not_of(t)+1);
  return s;
}

inline string& trim(string& s, const char* t = " \t\n\r\f\v") {
  return ltrim(rtrim(s, t), t);
}

int main() {
  string s;

  getline(cin, s);

  s = trim(s);
  
  vector<string> v = split(s, ' ');;
  
  cout << v.size();
}