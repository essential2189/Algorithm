import math

n = int(input())
money = list(map(int, input().split()))
m = int(input())

sum_money = sum(money)

if sum_money <= m:
    print(max(money))
else:
    check = [0 for _ in range(n)]

    limit = math.ceil(m / n)

    while True:
        total = 0
        for i in range(n):
            if money[i] < limit:
                total += money[i]
            else:
                total += limit

        if total == m:
            print(limit)
            break
        elif total > m:
            print(limit - 1)
            break

        limit += 1