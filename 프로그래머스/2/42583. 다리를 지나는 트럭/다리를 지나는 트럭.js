class Queue {
    constructor(init = []) {
        this.item = {}
        this.front = 0
        this.back = 0
        
        for (let i = 0; i < init.length; i++) {
            this.item[this.back] = init[i]
            this.back++
        }
    }
    
    size() {
        return this.back - this.front
    }
    
    pop_left() {
        if (this.size === 0) {
            return undefined
        }
        const p = this.item[this.front]
        delete this.item[this.front]
        this.front++
        return p
    }
    
    push(value) {
        this.item[this.back] = value
        this.back++
    }
    
    first() {
        return this.item[this.front]
    }
    
    [Symbol.iterator]() {
        let index = this.front;
        return {
            next: () => {
                if (index < this.back) {
                    return {value: this.item[index++], done: false}
                } else {
                    return {done: true}
                }
            }
        }
    }
}


function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let bridge = new Queue(Array.from({length: bridge_length}, () => 0))
    let bridge_weight = 0
    
    let queue = new Queue(truck_weights)
    
    answer++
    bridge.pop_left()
    
    let tw = queue.pop_left()
    bridge.push(tw)
    bridge_weight += tw
    
    while (bridge_weight > 0) {
        answer++
        
        bridge_weight -= bridge.pop_left()
        
        if (queue.size() > 0 && bridge_weight + queue.first() <= weight) {
            let p = queue.pop_left()
            bridge.push(p)
            bridge_weight += p
        } else {
            bridge.push(0)
        }
    }
    
    return answer
}