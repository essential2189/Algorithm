from collections import deque

N, K = map(int, input().split())

def bfs(N, K):
    q = deque()
    q.append(N)
    visited = [0] * 100001
    visited[N] = 1

    while q:
        current = q.popleft()

        if current == K:
            return visited[current]-1

        for move in (current+1, current-1, current*2):
            if 0 <= move < 100001 and visited[move] == 0:
                if move == current*2:
                    visited[move] = visited[current]
                    q.appendleft(move)
                else:
                    visited[move] = visited[current] + 1
                    q.append(move)

print(bfs(N, K))