def solution(N, K, time, important):
    dp = [[0] * (n + 1) for _ in range(k + 1)]

    for lecture_num in range(1, k+1):
        for now_time in range(1, n+1):
            if time[lecture_num-1] > now_time:
                dp[lecture_num][now_time] = dp[lecture_num-1][now_time]
            else:
                dp[lecture_num][now_time] = max(important[lecture_num-1] + dp[lecture_num-1][now_time - time[lecture_num-1]], dp[lecture_num-1][now_time])

    return dp[K][N]

n, k = map(int,input().split())
time = []
important = []
for _ in range(k):
    i, t = map(int,input().split())
    time.append(t)
    important.append(i)

print(solution(n, k, time, important))

