def div():
    nums = [True for _ in range(1000001)]

    for i in range(2, 1001):
        if nums[i]:
            for j in range(i * 2, 1000001, i):
                nums[j] = False
    return nums

def solution(n, nums):
    for i in range(3, len(nums)):
        if nums[i] and nums[n-i]:
            print("{} = {} + {}".format(n, i, n-i))
            break

nums = div()

while True:
    n = int(input())
    if n == 0:
        break
    solution(n, nums)


