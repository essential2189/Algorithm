T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j):
    queue = [[i, j]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < N and 0 <= y < M and board[x][y] == 1:
                board[x][y] = 0
                queue.append([x, y])


for _ in range(T):
    M, N, K = map(int, input().split())
    board = [[0]*M for i in range(N)]
    cnt = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        board[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                bfs(i, j)
                board[i][j] = 0
                cnt += 1
    print(cnt)
