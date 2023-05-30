def solution(sequence):
    answer = -1e9
    
    dp = {"+": [-float("Inf")], "-": [-float("Inf")]}
    
    for i, s in enumerate(sequence):
        if i % 2 == 0:
            dp["+"].append(max(dp["+"][i] + s, s))
            dp["-"].append(max(dp["-"][i] - s, -s))
        else:
            dp["+"].append(max(dp["+"][i] - s, -s))
            dp["-"].append(max(dp["-"][i] + s, s))
        
        answer = max(answer, dp["+"][-1], dp["-"][-1])
    
    return answer