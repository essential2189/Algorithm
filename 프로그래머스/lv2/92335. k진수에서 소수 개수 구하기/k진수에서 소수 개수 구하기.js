function convert(div, k, num) {
    let div_ = Math.floor(div / k)
    let remainder = div % k
    num += remainder.toString()
    if (div_ <= 0) {
        return num
    }
    
    num = convert(div_, k, num)
    
    return num
}

function solution(n, k) {
    let answer = 0;
    
    let div = Math.floor(n / k)
    let remainder = n % k
    let num = convert(div, k, remainder.toString())
    
    num = num.split("").reverse().join("")
    
    num_split = num.split("0")
    
    for (let n of num_split){
        n = Number(n)
        if (n && n !== 1) {
            let prime = true
            for (let i = 2; i <= Math.sqrt(n); i++) {
                if (n % i === 0) {
                    prime = false
                    break
                }
            }
            if (prime) {
                answer += 1
            }
        }
    }
    
    return answer;
}