from collections import deque

def bfs(graph, start, visited):
    q = deque([start])
    visited[start] = True
    count = 0
    
    while q:
        v = q.popleft()
        
        count += 1
        
        for node in graph[v]:
            if not visited[node]:
                q.append(node)
                visited[node] = True

    return count


def solution(n, wires):
    answer = n - 2
    
    for i in range(len(wires)):
        wire = wires[:]
        graph = [[] for _ in range(n+1)]
        visited = [False for _ in range(n+1)]
        del wire[i]
        
        for w in wire:
            x, y = w
            graph[x].append(y)
            graph[y].append(x)
            
        
        for idx, g in enumerate(graph):
            if len(g) > 0:
                start = idx
                break
                
        left_count = bfs(graph, start, visited)
        
        right_count = n - left_count
        
        if abs(left_count - right_count) < answer:
            answer = abs(left_count - right_count)
        
    return answer
        
        
                
    return answer