def count_board(board, max_):
    for i in range(len(board)):
        count_x = 1
        count_y = 1
        for j in range(len(board)-1):
            if board[i][j] == board[i][j+1]:
                count_x += 1
            else :
                count_x = 1

            if board[j][i] == board[j+1][i]:
                count_y += 1
            else :
                count_y = 1

            if count_x > count_y and count_x > max_:
                max_ = count_x

            if count_y > count_x and count_y > max_:
                max_ = count_y

            if max_ == N:
                return max_

    return max_

def solution(board, max_):
    max_ = count_board(board, max_)

    for i in range(len(board)):
        for j in range(len(board)-1):
            # 행 바꾸기
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            max_ = count_board(board, max_)
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

            # 열 바꾸기
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
            max_ = count_board(board, max_)
            board[j][i], board[j+1][i] = board[j+1][i], board[j][i]

            if max_ == N:
                return max_

    return max_

N = int(input())

board = []

for _ in range(N):
    board.append([*input()])

max_ = 0

max_ = solution(board, max_)
print(max_)
