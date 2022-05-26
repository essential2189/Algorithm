def solution():
    nums = input().split()
    nums_int = [int(i) for i in nums]
    answer = 0
    for n in nums_int:
        if n % 2 != 0:
            answer += n

    return answer

for t in range(int(input())):
    answer = solution()

    print("#{} {}".format(t+1, answer))