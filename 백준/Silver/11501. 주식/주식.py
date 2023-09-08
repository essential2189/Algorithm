import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    prices = list(map(int, input().split(" ")))
    prices = prices[::-1]
    max_prices = 0
    answer = 0

    for p in prices:
        if p > max_prices:
            max_prices = p
        else:
            answer += max_prices - p

    print(answer)
