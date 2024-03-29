function solution(numbers) {
    var answer = '';
    
    numbers.sort((a, b) => {
        let aa = a.toString()
        let bb = b.toString()
        
        return (bb + aa) - (aa + bb)
    })
    
    if (numbers[0] === 0) {
        return "0"
    }
    
    return numbers.join("");
}