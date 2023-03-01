n = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

answer = 0
min_ = price[0]
for i in range(n-1):
    if price[i] < min_:
        min_ = price[i]
    answer += min_ * distance[i]

print(answer)