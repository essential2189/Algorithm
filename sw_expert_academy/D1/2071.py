def solution():
    nums = input().split()

    nums_int = [int(i) for i in nums]

    sum = 0

    for n in nums_int:
        sum += n
    # print(sum)

    str_sum = str(sum)
    if int(str_sum[-1]) >= 5:
        return sum // 10 + 1

    elif 0 <= int(str_sum[-1]) <= 4:
        return sum // 10




for t in range(int(input())):
    answer = solution()

    print("#{} {}".format(t+1, answer))