def solution(items):
    for i in range(1, N+1):
        for j in range(1, K+1):
            w, v = items[i]
            print(w, v)

            if j < w:
                bag[i][j] = bag[i-1][j]
                print(bag)
            else:
                bag[i][j] = max(v + bag[i-1][j-w], bag[i-1][j])
                print(bag)

    return bag[N][K]

N, K = map(int, input().split(" "))

bag = [[0 for _ in range(K+1)] for _ in range(N+1)]
items = [[0,0]]
for _ in range(N):
    W, V = map(int, input().split(" "))
    items.append([W, V])


print(solution(items))
