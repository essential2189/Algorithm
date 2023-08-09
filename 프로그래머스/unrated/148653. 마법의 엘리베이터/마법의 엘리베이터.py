def solution(storey):
    answer = 0

    while storey:
        div = storey % 10
        
        if div > 5:
            answer += 10 - div
            storey += 10 - div
            
        elif div < 5:
            answer += div
        
        else:
            if (storey // 10) % 10 > 4:
                storey += 10 - div
            answer += div
            
        storey //= 10
            
            
    return answer
