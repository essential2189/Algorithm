def solution(N, M, button):

    min_count = abs(100-N)

    for i in range(1000001):
        num = str(i)

        for j in range(len(num)):

            if int(num[j]) in button:
                break

            elif len(num) == j+1:
                min_count = min(min_count, abs(int(num) - N) + len(num))

    print(min_count)


N = int(input())
M = int(input())
button = []
if M > 0:
    button = list(map(int, input().split()))

solution(N, M, button)