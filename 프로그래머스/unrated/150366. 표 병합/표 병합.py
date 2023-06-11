def solution(commands):
    answer = []
    board = [["EMPTY"] * 50 for _ in range(50)]
    merged = [[(i, j) for j in range(50)] for i in range(50)]
    
    for command in commands:
        com = command.split(" ")
        
        if com[0] == "UPDATE":
            if len(com) == 4:
                _, r, c, value = com
                x, y = merged[int(r)-1][int(c)-1]
                board[x][y] = value

            elif len(com) == 3:
                _, value1, value2 = com
                for i in range(50):
                    for j in range(50):
                        if board[i][j] == value1:
                            board[i][j] = value2
        
        elif com[0] == "MERGE":
            _, r1, c1, r2, c2 = com
            x1,y1 = merged[int(r1)-1][int(c1)-1]
            x2,y2 = merged[int(r2)-1][int(c2)-1]
            if board[x1][y1] == "EMPTY":
                board[x1][y1] = board[x2][y2]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x2,y2):
                        merged[i][j] = (x1,y1)
            
        elif com[0] == "UNMERGE":
            _, r, c = com
            x, y = merged[int(r)-1][int(c)-1]
            tmp = board[x][y]
            for i in range(50):
                for j in range(50):
                    if merged[i][j] == (x,y):
                        merged[i][j] = (i,j)
                        board[i][j] = "EMPTY"
            board[int(r)-1][int(c)-1] = tmp
            
        elif com[0] == "PRINT":
            _, r, c = com
            x, y = merged[int(r)-1][int(c)-1]
            answer.append(board[x][y])

    return answer