def solution(n):
    answer = 0
    board = []
    for _ in range(n):
        board.append(input())

    center = n // 2

    for i in range(n):
        if i <= center:
            for j in board[i][center - i:center + 1 + i]:
                answer += int(j)
        else:
            for j in board[i][i - center: n - i + center]:
                answer += int(j)

    return answer

for t in range(1, int(input())+1):
    answer = solution(int(input()))

    print("#{} {}".format(t, answer))