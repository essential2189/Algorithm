from collections import deque

def check(board):
    q = deque()
    
    temp1 = list(board[0])
    temp2 = list(board[1])
    temp3 = list(board[2])
    temp4 = list(zip(*board))[0]
    temp5 = list(zip(*board))[1]
    temp6 = list(zip(*board))[2]
    temp7 = []
    temp8 = []
    
    for i in range(3):
        temp7.append(board[i][i])
        temp8.append(board[i][2-i])
        
    temp = [temp1, temp2, temp3, temp4, temp5, temp6, temp7, temp8]
    
    winner = [False, False]
    for t in temp:
        if t.count("O") == 3:
            winner[0] = "O"
        if t.count("X") == 3:
            winner[1] = "X"
        
    return winner
            
                
def solution(board):
    winner = check(board)
    
    o = 0
    x = 0
    
    for b in board:
        o += b.count("O")
        x += b.count("X")
        
    if o == x:
        if winner[0] == "O":
            return 0
        else:
            return 1
    elif o - x == 1:
        if winner[0] == "O" and not winner[1]:
            return 1
        elif winner[1] == "X":
            return 0
        else:
            return 1
    else:
        return 0
    
    return -1