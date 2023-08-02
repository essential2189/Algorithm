from collections import deque

def solution(maps):
    answer = 9999999
    
    dist = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    q = deque()
    
    lever_dist = 9999999
    lever_x = 0
    lever_y = 0
    flag = False
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                q.append([i, j, 1, False])
                
            while q:
                y, x, cnt, lever = q.popleft()
                
                for d in dist:
                    yy = y + d[0]
                    xx = x + d[1]
                    
                    if 0 <= yy < len(maps) and 0 <= xx < len(maps[0]) and maps[yy][xx] != "X" and not visited[yy][xx]:
                        if maps[yy][xx] == "L":
                            if cnt < lever_dist:
                                lever_dist = cnt
                                lever_x = xx
                                lever_y = yy
                                flag = True
                            
                        else:
                            q.append([yy, xx, cnt+1, lever])
                            visited[yy][xx] = True

    if not flag:
        return -1
    
    flag = False
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    
    q = deque()
    q.append([lever_y, lever_x, lever_dist])
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
                
            while q:
                y, x, cnt = q.popleft()
                
                for d in dist:
                    yy = y + d[0]
                    xx = x + d[1]
                    
                    if 0 <= yy < len(maps) and 0 <= xx < len(maps[0]) and maps[yy][xx] != "X" and not visited[yy][xx]:
                        if maps[yy][xx] == "E":
                            if cnt < answer:
                                answer = cnt+1
                                flag = True
                            
                        else:
                            q.append([yy, xx, cnt+1])
                            visited[yy][xx] = True
    if not flag:
        return -1
    
    return answer
