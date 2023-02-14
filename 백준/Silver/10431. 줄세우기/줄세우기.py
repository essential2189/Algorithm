def solution(nums):
    num = nums[0]

    h_list = [nums[1]]
    count = 0
    for h in nums[2:]:
        flag = False
        for i in range(len(h_list)):
            if h < h_list[i]:
                count += len(h_list) - i
                h_list.insert(i, h)
                flag = True
                break

        if flag == False:
            h_list.append(h)

    if len(h_list) == 0:
        return "{0} {1}".format(num, count)
    return "{0} {1}".format(num, count)

N = int(input())

for _ in range(N):
    print(solution(list(map(int, input().split()))))