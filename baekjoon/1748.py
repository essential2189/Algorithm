def solution(N):
    answer = 0

    l = len(str(N))

    for i in range(l-1):
        answer += 9 * (10 ** i) * (i + 1)
        i += 1

    answer += ((N - 10 ** (l-1)) + 1) * l

    print(answer)


solution(int(input()))

