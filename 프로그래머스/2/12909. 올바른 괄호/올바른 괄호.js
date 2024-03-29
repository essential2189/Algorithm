function solution(s){
    let stack = []

    for (const i of s) {
        if (i === "(") {
            stack.push(i)
        } else {
            if (stack.length > 0) {
                stack.pop()
            } else {
                stack.push(i)
            }
        }
    }
    
    if (stack.length > 0) {
        return false
    }

    return true;
}