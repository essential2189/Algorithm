import sys

input = sys.stdin.readline

string_left = list(input().strip())
string_right = []

m = int(input())



for _ in range(m):
    c = input().strip().split(" ")

    if c[0] == "L":
        if string_left:
            string_right.append(string_left.pop())

    elif c[0] == "D":
        if string_right:
            string_left.append(string_right.pop())

    elif c[0] == "B":
        if string_left:
            string_left.pop()

    elif c[0] == "P":
        string_left.append(c[1])

answer = string_left + string_right[::-1]

print("".join(answer))
