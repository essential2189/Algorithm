def solution(items):


N, K = map(int, input().split(" "))

items = []
for _ in range(N):
    W, V = map(int, input().split(" "))
    items.append([W, V])

solution(items)
