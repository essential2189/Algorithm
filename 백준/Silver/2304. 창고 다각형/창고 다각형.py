import sys
input = sys.stdin.readline

max_h = 0
max_i = 0
pli = [0 for _ in range(1001)] # 기둥

for _ in range(int(input())):
    l, h = map(int, input().split())
    pli[l] = h
    if max_h < h: # 가장 높은 기둥과 그 기둥의 인덱스를 찾음
        max_i = l
        max_h = h

h = 0
answer = 0

for i in range(max_i+1):
    h = max(h, pli[i])
    answer += h

h = 0

for i in range(1000, max_i, -1):
    h = max(h, pli[i])
    answer += h

print(answer)
