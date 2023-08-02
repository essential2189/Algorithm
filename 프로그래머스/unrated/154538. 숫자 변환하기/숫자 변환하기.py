from collections import deque

def solution(x, y, n):
    q = deque([[x, 0]])
    visited = [False for _ in range(y+1)]
    
    while q:
        a, cnt = q.popleft()
        
        if a == y:
            return cnt
        
        if a+n <= y and not visited[a+n]:
            q.append([a+n, cnt+1])
            visited[a+n] = True
        
        if a*2 <= y and not visited[a*2]:
            q.append([a*2, cnt+1])
            visited[a*2] = True
        
        if a*3 <= y and not visited[a*3]:
            q.append([a*3, cnt+1])
            visited[a*3] = True
    
    return -1