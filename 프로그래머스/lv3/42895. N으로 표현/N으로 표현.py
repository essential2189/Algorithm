def solution(N, number):
    if N == number:
        return 1
    
    dp = []
    
    for c in range(1, 9):
        partial_set = set([int(str(N) * c)])
        for i in range(len(dp)):
            num1 = dp[i]
            num2 = dp[-i - 1]
            
            for n1 in num1:
                for n2 in num2:
                    partial_set.add(n1 + n2)
                    partial_set.add(n1 - n2)
                    partial_set.add(n2 - n1)
                    partial_set.add(n1 * n2)
                    if n1 != 0:
                        partial_set.add(n2//n1)
                    if n2 != 0:
                        partial_set.add(n1//n2)
        
        if number in partial_set:
            return c
        dp.append(partial_set)
        
    return -1