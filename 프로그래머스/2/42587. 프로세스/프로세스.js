class Queue{
    constructor(init = []) {
        this.queue = {}
        this.front = 0
        this.back = 0
        
        for (const i of init) {
            this.queue[this.back] = i
            this.back++
        }
    }
    
    size() {
        return this.back - this.front
    }
    
    popleft() {
        let pop = this.queue[this.front]
        delete this.queue[this.front]
        this.front++
        return pop
    }
    
    push(value) {
        this.queue[this.back] = value
        this.back++
    }
    
    index(index) {
        return this.queue[this.front + index];
    }
    
    print() {
        let temp = []
        for (let i = 0; i < this.size(); i++) {
            temp.push(this.index(i))
        }
        
        console.log(temp)
    }

}

function solution(priorities, location) {
    var answer = 0;
    
    let queue = new Queue(priorities)
    
    while (queue.size() > 0) {
        let flag = true
        let q = queue.popleft()
        
        
        for (let i = 0; i < queue.size(); i++) {
            if (queue.index(i) > q) {
                queue.push(q)
                flag = false
                break;
            }
        }
        
        if (flag) {
            answer += 1

            if (location === 0) {
                return answer
            }
        }    
        
        if (location === 0) {
            location = queue.size()
        }
        
        location--
    }
    
    return answer;
}