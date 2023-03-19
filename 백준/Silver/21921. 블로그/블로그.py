import sys
input=sys.stdin.readline

n, x = map(int, input().split())

visitor = list(map(int, input().split()))



if max(visitor) == 0:
    print("SAD")
else:

    sum_ = sum(visitor[:x])

    max_ = sum_
    count = 1

    for i in range(x, n):
        sum_ += visitor[i]
        sum_ -= visitor[i-x]

        if max_ < sum_:
            max_ = sum_
            count = 1
        elif max_ == sum_:
            count += 1

    print(max_)
    print(count)