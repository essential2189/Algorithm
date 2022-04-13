from sys import stdin

def solution():
    N = int(input())

    words = []
    for _ in range(N):
        words.append(stdin.readline().strip())

    words = list(set(words))
    words.sort()
    words.sort(key = len)

    return words

answer = solution()
for a in answer:
    print(a)