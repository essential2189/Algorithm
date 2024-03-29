# https://velog.io/@gkscodus11/%EB%B0%B1%EC%A4%80-17208-%EC%B9%B4%EC%9A%B0%EB%B2%84%EA%B1%B0-%EC%95%8C%EB%B0%94%EC%83%9D

# 완전 탐색
# def knapsack(idx, burger, fry):
#     if idx == n:
#       return 0
#     ret = 0
#
#     if burger >= order[idx][0] and fry >= order[idx][1]:
#         ret = 1 + knapsack(idx + 1, burger - order[idx][0], fry - order[idx][1])
#
#     ret = max(ret, knapsack(idx + 1,burger, fry))
#
#     return ret

def knapsack(idx, burger, fry):
    if idx == n:    # 더 이상 주문이 없음
        return 0
    if dp[idx][burger][fry] != -1:  # 이전에 계산한적이 있는 경우
        return dp[idx][burger][fry]
    dp[idx][burger][fry] = 0

    if burger >= order[idx][0] and fry >= order[idx][1]:    # 남아 있는 버거랑 감튀가 주문량 보다 많을 경우 주문 처리 가능
        dp[idx][burger][fry] = 1 + knapsack(idx + 1, burger - order[idx][0], fry - order[idx][1])    # 주문을 받을 경우, 해당 계산을 dp에 저장

    # max(주문을 받을 경우, 주문을 받지 않을 경우)
    # 남은 버거랑 감튀가 주문량보다 적으면 ret=0이기에 주문을 받지 않은 경우가 무조건 당선
    dp[idx][burger][fry] = max(dp[idx][burger][fry], knapsack(idx + 1, burger, fry))    # 해당 계산을 dp에 저장

    return dp[idx][burger][fry]

n, m, k = list(map(int, input().split()))

order = [list(map(int, input().split())) for _ in range(n)]

# dp[주문번호][남은 치즈버거][남은 감자튀김]
dp = [[[-1] * (k+1) for _ in range(m+1)] for _ in range(n)]
print(knapsack(0, m, k))
