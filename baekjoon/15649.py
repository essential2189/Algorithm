s = []

def dfs(N, M):
    if len(s) == M:
        print(" ".join(map(str, s)))
        return

    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            dfs(N, M)
            s.pop()


def solution(str):
    N, M = map(int, str.split(" "))

    dfs(N, M)


solution(input())