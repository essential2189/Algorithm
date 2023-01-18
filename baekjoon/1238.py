import heapq

def dijkstra(start):
    D = [float("inf")] * (N+1)
    D[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        dist, now = heapq.heappop(heap)
        if D[now] >= dist:
            for node_b, t in city[now]:
                if dist + t < D[node_b]:
                    D[node_b] = dist + t
                    heapq.heappush(heap, (dist + t, node_b))

    return D


N, M, X = map(int, input().split())

city = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, t = map(int, input().split())
    city[a].append((b, t))

answer = dijkstra(X) # X에서 출발해서 각 도착지(1~N+1)로 도착하는 경로 비용 계산
answer[0] = 0
for i in range(1, N+1):
    res = dijkstra(i) # 출발지(1~N+1)에서 각 도착지(1~N+1)에 도착하는 경로 비용 계산
    answer[i] += res[X] # X로 도착하는 비용 추출하여 더하기

print(max(answer))