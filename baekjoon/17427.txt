def solution():
    num = int(input())

    sum = 0

    for i in range(1, num+1):
        sum += (num // i) * i

    return sum

print(solution())