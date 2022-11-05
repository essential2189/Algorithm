def solution(N):
    num = list(map(int, N.split(" ")))

    MAX = 10000
    div = []
    mul = 0

    max_num = max(num)
    min_num = min(num)

    for i in range(1, max_num+1):
        if num[0] % i == 0 and num[1] % i == 0:
            div.append(i)

    i = min_num
    while True:
        if i % num[0] == 0 and i % num[1] == 0:
            mul = i
            break
        i += min_num

    print(max(div))
    print(mul)


solution(input())
