def dfs(N, M):
    if len(s) == M:
        s_sort = sorted(s)
        if s_sort not in visited:
            print(" ".join(map(str, s)))
        visited.append(s.copy())
        return

    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            dfs(N, M)
            s.pop()



N, M = map(int, input().split(" "))
s = []
visited = []
dfs(N, M)


