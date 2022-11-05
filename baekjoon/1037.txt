def solution():
    num_list = list(map(int, input().split(" ")))

    max_num = max(num_list)
    min_num = min(num_list)


    return max_num * min_num

temp = input()

print(solution())