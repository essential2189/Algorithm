import sys

input = sys.stdin.readline

n, m = map(int, input().split(" "))

keyword = {}
blog = []


for _ in range(n):
    key = input().strip()
    keyword[key] = 0

answer = n
for _ in range(m):
    blog = input().strip().split(",")

    for b in blog:
        if b in keyword:
            del keyword[b]
            answer -= 1

    print(answer)