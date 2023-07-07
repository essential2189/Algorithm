function makeBoard(rows, columns) {
    let board = Array.from({ length: rows }, () => []);
    
    let count = 1
    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            board[i].push(count)
            count += 1
        }
    }
    
    return board
}

function getBorder(board, x1, y1, x2, y2){
    let border = [0]
    let x = x1
    let y = y1
    
    while (true) {
        if (x === x1 || x === x2 || y === y1 || y === y2){
            border.push(board[y][x])
        }

        if (y === y1 && x1 <= x && x < x2) {
            x++
        } else if (x === x2 && y1 <= y && y < y2) {
            y++
        } else if (y === y2 && x1 < x && x <= x2) {
            x--
        } else if (x === x1 && y1 < y && y <= y2){
            y--
        }

        if (x === x1 && y === y1){
            break
        }
    }
    return border
}

function rotationBoard(board, border, x1, y1, x2, y2){
    let idx = 0
    let x = x1
    let y = y1
    
    while (true) {
        if (x === x1 || x === x2 || y === y1 || y === y2){
            board[y][x] = border[idx]
            idx++
        }

        if (y === y1 && x1 <= x && x < x2) {
            x++
        } else if (x === x2 && y1 <= y && y < y2) {
            y++
        } else if (y === y2 && x1 < x && x <= x2) {
            x--
        } else if (x === x1 && y1 < y && y <= y2){
            y--
        }
        
        if (x === x1 && y === y1){
            break
        }
    }
    
    return board
}

function solution(rows, columns, queries) {
    let answer = [];
    
    let board = makeBoard(rows, columns)
    
    for (const query of queries) {
        let y1 = query[0] - 1
        let x1 = query[1] - 1
        let y2 = query[2] - 1
        let x2 = query[3] - 1

        let border = getBorder(board, x1, y1, x2, y2)
        
        border[0] = border[border.length - 1]
        border.pop()
        board = rotationBoard(board, border, x1, y1, x2, y2)
        
        answer.push(Math.min(...border))
    }
    
    return answer;
}