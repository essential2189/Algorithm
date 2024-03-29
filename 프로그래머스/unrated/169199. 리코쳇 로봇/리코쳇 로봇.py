from collections import deque

def solution(board):
    answer = 999999999
    
    dist = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    
    q = deque()
    flag = False
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "R":
                q.append([i, j, 0])
            
            while q:
                y, x, count = q.popleft()
                if board[y][x] == "G":
                    if count < answer:
                        flag = True
                        answer = count
                
                for dy, dx in dist:
                    yy = y
                    xx = x
                    while True:
                        yy += dy
                        xx += dx
                        if 0 > yy or yy >= len(board) or 0 > xx or xx >= len(board[0]) or board[yy][xx] == "D":
                            yy -= dy
                            xx -= dx
                            
                            break
                    
                    if not visited[yy][xx]:
                        visited[yy][xx] = True
                        q.append([yy, xx, count+1]) 
      
    if flag:
        return answer
    return -1