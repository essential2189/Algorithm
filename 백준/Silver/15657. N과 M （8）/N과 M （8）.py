import sys

sys.setrecursionlimit(10 ** 5)


def dfs(start):
    if len(stack) == m:
        print(*stack)
        return
    for i in range(start, n):
        stack.append(nums[i])
        dfs(i)
        stack.pop()

    return


n, m = list(map(int, input().split()))
nums = sorted(list(map(int, input().split())))
stack = []
dfs(0)
