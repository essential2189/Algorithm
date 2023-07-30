def solution(scores):
    answer = 0   
    
    target_s1, target_s2 = scores[0][0], scores[0][1]
    target_score = scores[0][0] + scores[0][1]
    
    scores.sort(key=lambda x:(-x[0], x[1]))
    
    max_s2 = 0
    
    for s1, s2 in scores:
        if target_s1 < s1 and target_s2 < s2:
            return -1
        
        if s2 >= max_s2:
            max_s2 = s2
            if s1 + s2 > target_score:
                answer += 1
                
    return answer + 1