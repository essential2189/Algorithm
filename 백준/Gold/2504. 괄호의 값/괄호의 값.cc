#include <iostream>
#include <string>
#include <deque>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

  string str;

  cin >> str;

  deque<char> stack;

  for (int i = 0; i < str.length(); i++) {
    if (str[i] == '(') {
      stack.push_back('(');
    } else if (str[i] == ')') {
      if (!stack.empty() && stack.back() == '(') {
        stack.pop_back();
      } else {
        stack.push_back(')');
      }
    } else if (str[i] == '[') {
      stack.push_back('[');
    } else if (str[i] == ']') {
      if (!stack.empty() && stack.back() == '[') {
        stack.pop_back();
      } else {
        stack.push_back(']');
      }
    }
  }

  if (stack.size() > 0) {
    cout << 0;
    return 0;
  }


  int answer = 0;
  deque<string> s;

  for (int i = 0; i < str.length(); i++) {
    if (str[i] == '(') {
      s.push_back("(");
    } else if (str[i] == '[') {
      s.push_back("[");
    } else if (str[i] == ')') {
      if (s.back() == "(") {
        s.pop_back();
        s.push_back("2");
      } else {
        int temp = 0;
        while(s.back() != "(") {
          temp += stoi(s.back());
          s.pop_back();
        }
        s.pop_back();
        s.push_back(to_string(temp*2));
      }
    } else if (str[i] == ']') {
      if (s.back() == "[") {
        s.pop_back();
        s.push_back("3");
      } else {
        int temp = 0;
        while(s.back() != "[") {
          temp += stoi(s.back());
          s.pop_back();
        }
        s.pop_back();
        s.push_back(to_string(temp*3));
      }
    }
  }



  for (int i = 0; i < s.size(); i++) {
    answer += stoi(s[i]);
  }

  cout << answer;
}