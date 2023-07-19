function solution(name, yearning, photo) {
    var answer = new Array(photo.length).fill(0);
    
    let map = {}
    
    
    for (let i = 0; i < name.length; i++) {
        map[name[i]] = yearning[i]
    }
    
    for (let i = 0; i < photo.length; i++) {
        let sum = 0
        for (const p of photo[i]) {
            if (p in map) {
                sum += map[p]
            }
        }
        answer[i] = sum
    }
    
    
    return answer;
}