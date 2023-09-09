import sys

input = sys.stdin.readline

n = int(input())

arr = []

left_peaple = list(map(int, input().split()))[::-1]

for i, p in enumerate(left_peaple):
    arr.insert(p, n - i)

print(*arr)
