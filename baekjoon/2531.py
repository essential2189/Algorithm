belt, num, K, coupon = map(int, input().split())

items = []
for _ in range(belt):
    items.append(int(input()))

items += items[:K-1]
max_len = 0
for i in range(len(items)-K+1):
    set_ = set()
    for j in range(i, i+K):
        set_.add(items[j])

    set_.add(coupon)
    max_len = max(max_len, len(set_))
print(max_len)