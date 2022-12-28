def solution(N):
    if N == 1:
        return 1

    elif N == 2:
        return 2

    elif N == 3:
        return 4

    else:
        return solution(N-1) + solution(N-2) + solution(N-3)


T = int(input())
for _ in range(T):
    print(solution(int(input())))

