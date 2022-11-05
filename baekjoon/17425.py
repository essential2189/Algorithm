import sys

def solution():
    MAX = 1000000

    dp = [0] * (MAX + 1)
    sum_list = [0] * (MAX + 1)

    for i in range(1, MAX+1):
        j = 1
        while i * j <= MAX:
            dp[i * j] += i
            j += 1
        sum_list[i] = sum_list[i-1] + dp[i]

    return sum_list

T = int(input())

sum_list = solution()

for _ in range(T):
    n = int(sys.stdin.readline())

    print(sum_list[n])
