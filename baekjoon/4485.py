import heapq

def dijkstra():
    q = []
    heapq.heappush(q, [0, 0])
    cost[0][0] = board[0][0]

    dist = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while q:
        [y, x] = heapq.heappop(q)

        if [y, x] == [N-1, N-1]:
            print(f"Problem {count}: {cost[N-1][N-1]}")
            break

        for dx, dy in dist:
            if 0 <= y + dy < N and 0 <= x + dx < N:
                new_cost = cost[y][x] + board[y + dy][x + dx]
                if cost[y + dy][x + dx] > new_cost:
                    cost[y + dy][x + dx] = new_cost
                    heapq.heappush(q, [y + dy, x + dx])


count = 1
while True:
    N = int(input())
    if N == 0:
        break

    board = [list(map(int, input().split())) for _ in range(N)]
    cost = [[float("inf") for _ in range(N)] for _ in range(N)]

    dijkstra()
    count += 1
