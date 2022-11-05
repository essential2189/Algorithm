def solution():
    A, B = map(int, input().split(" "))
    nums = set([1])

    for i in range(2, B*2):
        for j in range(i*2, B*2, i):
            nums.add(j)

    # print(nums)
    for i in range(A, B+1):
        if i not in nums:
            print(i)

solution()
