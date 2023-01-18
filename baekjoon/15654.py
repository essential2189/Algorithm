N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

s = []

def backtracking(depth):
    # if len(s) == M:
    #     print(" ".join(map(str, s)))
    #     return
    if depth == M:
        print(" ".join(map(str, s)))
        return

    for i in range(N):
        if nums[i] in s:
            continue
        s.append(nums[i])
        backtracking(depth+1)
        s.pop()

backtracking(0)