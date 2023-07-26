def solution(park, routes):
    answer = []
    board = []
    
    for p in park:
        board.append(list(p))
        
        
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "S":
                y = i
                x = j
                
    for r in routes:
        direc, dist = r.split(" ")
        yy = y
        xx = x
        
        for _ in range(int(dist)):
            if (direc == "N"):
                y -= 1
                if 0 > x or x >= len(board[0]) or 0 > y or y >= len(board) or board[y][x] == "X":
                    y = yy
                    break
            
            if (direc == "S"):
                y += 1
                if 0 > x or x >= len(board[0]) or 0 > y or y >= len(board) or board[y][x] == "X":
                    y = yy
                    break
            if (direc == "E"):
                x += 1
                if 0 > x or x >= len(board[0]) or 0 > y or y >= len(board) or board[y][x] == "X":
                    x = xx
                    break
            if (direc == "W"):
                x -= 1
                if 0 > x or x >= len(board[0]) or 0 > y or y >= len(board) or board[y][x] == "X":
                    x = xx
                    break
    
    return [y, x]


# "OSO",
# "OOO",
# "OXO", 
# "OOO"]