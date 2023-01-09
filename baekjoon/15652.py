stack = []

def solution(start):
    if len(stack) == M:
        print(" ".join(map(str, stack)))
        return

    for i in range(start, N+1):
        stack.append(i)
        solution(i)
        stack.pop()

N, M = map(int, input().split(" "))
solution(1)
