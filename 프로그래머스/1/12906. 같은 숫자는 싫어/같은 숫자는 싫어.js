function solution(arr)
{
    var answer = [];
    
    while (arr.length > 0) {
        let pop = arr.pop()
        
        if (arr[arr.length-1] !== pop) {
            answer.push(pop)
        }
    }
    
    return answer.reverse();
}