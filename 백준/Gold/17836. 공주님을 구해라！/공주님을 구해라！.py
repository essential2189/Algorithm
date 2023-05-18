from collections import deque

def solution(n, m, t, board):
    dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True
    q = deque([[0, 0, 0]])
    answer = float("inf")

    while q:
        y, x, time = q.popleft()
        if y == n-1 and x == m-1:
            answer = min(answer, time)
            break

        if time + 1 > t:
            break

        for dx, dy in dir:
            yy = y + dy
            xx = x + dx

            if 0 <= yy < n and 0 <= xx < m and not visited[yy][xx]:
                if board[yy][xx] == 0:
                    visited[yy][xx] = True
                    q.append([yy, xx, time+1])

                elif board[yy][xx] == 2:    # 그람 찾음
                    visited[yy][xx] = True
                    temp = time + 1     # 그람까지 온 거리
                    temp += abs(n - 1 - yy) + abs(m - 1 - xx)   # 그람에서 공주까지의 거리
                    if temp <= t:
                        answer = temp

    if answer > t:
        return "Fail"
    else:
        return answer

n, m, t = list(map(int, input().split()))
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

print(solution(n, m, t, board))
