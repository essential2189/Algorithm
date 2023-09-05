import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))

title = []
power = []

for _ in range(n):
    t, p = input().split(" ")
    p = int(p)

    # 가장 처음 칭호만 저장해주기 위해 이전에 append한 값이랑 같을 때 continue
    if power and power[-1] == power:
        continue

    title.append(t)
    power.append(p)


def binary_search(p):
    left = 0
    right = len(power) - 1

    # right를 p보다 작게 만드는게 중요
    while left <= right:
        mid = (left + right) // 2
        if p > power[mid]:
            left = mid + 1
        else:
            right = mid - 1
        
    print(title[right+1])

for _ in range(m):
    p = int(input())
    binary_search(p)