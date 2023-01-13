stack = []
def solution(N, M):
    if len(stack) == M:
        print(" ".join(map(str, stack)))
        return

    for i in range(1, N+1):
        stack.append(i)
        solution(N, M)
        stack.pop()

N, M = map(int, input().split(" "))
solution(N, M)
