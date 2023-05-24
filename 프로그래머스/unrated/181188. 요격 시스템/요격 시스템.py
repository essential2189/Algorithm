def solution(targets):
    answer = 0
    
    targets.sort(key = lambda x: [x[1], x[0]])

    target_in = 0
    for t in targets:
        if t[0] >= target_in:
            answer += 1
            target_in = t[1]
    
    return answer