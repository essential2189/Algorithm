def solution() :
    N, M = map(int, input().split())

    min_ = []

    board_full = []
    for _ in range(N):
        board_full.append(input())


    for n in range(N-7):
        for m in range(M - 7):
            count1 = 0
            count2 = 0
            for i in range(8):
                if i % 2 == 0:
                    count1 += board_full[n:n + 8][i][m:m + 8:2].count("W")
                    count1 += board_full[n:n + 8][i][m+1:m + 9:2].count("B")
                else:
                    count1 += board_full[n:n + 8][i][m:m + 8:2].count("B")
                    count1 += board_full[n:n + 8][i][m + 1:m + 9:2].count("W")

                if i % 2 == 0:
                    count2 += board_full[n:n + 8][i][m:m + 8:2].count("B")
                    count2 += board_full[n:n + 8][i][m+1:m + 9:2].count("W")
                else:
                    count2 += board_full[n:n + 8][i][m:m + 8:2].count("W")
                    count2 += board_full[n:n + 8][i][m + 1:m + 9:2].count("B")

            min_.append(min(count1, count2))
    answer = min(min_)
    return answer



count_f = solution()
print(count_f)