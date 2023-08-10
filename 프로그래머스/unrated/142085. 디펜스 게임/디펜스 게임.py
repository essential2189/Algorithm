import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    sum_enemy = 0
    
    for e in enemy:
        heapq.heappush(heap, -e)
        sum_enemy += e
        if sum_enemy > n:
            if k == 0:
                break
            sum_enemy -= -heapq.heappop(heap)
            k -= 1
        answer += 1
        
    return answer