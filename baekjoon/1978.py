def solution():
    n = list(map(int, input().split(" ")))
    nums = [1]

    for i in range(2, 1000+1):
        for j in range(i*2, 1000+1, i):
            if j not in nums:
                nums.append(j)

    # print(sorted(nums))
    count = 0
    for i in n:
        if i not in nums:
            count += 1
    return count

N = int(input())

print(solution())
