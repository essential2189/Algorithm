import heapq

def solution():
    n = int(input())
    nums = input().split()

    nums_min = [int(i) for i in nums]
    nums_max = [-int(i) for i in nums]

    heapq.heapify(nums_min)
    heapq.heapify(nums_max)

    for _ in range(n):
        max_ = heapq.heappop(nums_max)
        min_ = heapq.heappop(nums_min)

        temp_max = max_ + 1
        temp_min = min_ + 1

        heapq.heappush(nums_max, temp_max)
        heapq.heappush(nums_min, temp_min)

    max_ = heapq.heappop(nums_max)
    min_ = heapq.heappop(nums_min)
    return -max_ - min_

for t in range(10):
    answer = solution()

    print("#{} {}".format(t+1, answer))