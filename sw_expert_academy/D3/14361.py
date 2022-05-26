def solution():
    n = int(input())

    str_n = [i for i in str(n)]

    str_n.sort()

    sum_ = n
    sum_list = []

    while len(str(sum_)) == len(str_n):
        sum_ += n
        sum_list.append(str(sum_))


    for s in sum_list:
        if sorted(s) == str_n:
            return "possible"

    return "impossible"


for t in range(int(input())):
    result = solution()

    print("#{} {}".format(t+1, result))