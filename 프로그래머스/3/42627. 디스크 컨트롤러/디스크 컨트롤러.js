class Heap {
    constructor(init = []){
        this.heap = []
        
        for (const i of init) {
            this.heappush(i)
        }
    }
    
    getParentIndex(index) {
        return Math.floor((index - 1) / 2)
    }
    
    getLeftChildIndex(parentIndex) {
        return parentIndex * 2 + 1
    }
    
    getRightChildIndex(parentIndex) {
        return parentIndex * 2 + 2
    }
    
    swap(index1, index2) {
        [this.heap[index1], this.heap[index2]] = [this.heap[index2], this.heap[index1]]
    }
    
    heappush(value) {
        this.heap.push(value)
        this.heapifyUp()
    }
    
    heapifyUp() {
        let index = this.heap.length - 1
        
        while (index > 0 && this.heap[this.getParentIndex(index)][1] > this.heap[index][1]) {
            this.swap(this.getParentIndex(index), index)
            index = this.getParentIndex(index)
        }
    }
    
    heappop() {
        if (this.heap.length === 0) {
            return null
        }
        
        const root = this.heap[0]
        
        this.heap[0] = this.heap[this.heap.length-1]
        this.heap.pop()
        this.heapifyDown()
        
        return root
    }
    
    heapifyDown() {
        let index = 0
        
        while (this.getLeftChildIndex(index) < this.heap.length) {
            let smallerChildIndex = this.getLeftChildIndex(index)
            
            if (this.getRightChildIndex(index) < this.heap.length && this.heap[this.getRightChildIndex(index)][1] < this.heap[smallerChildIndex][1]) {
                smallerChildIndex = this.getRightChildIndex(index)
            }
            
            if (this.heap[index][1] < this.heap[smallerChildIndex][1]) {
                break
            } else {
                this.swap(index, smallerChildIndex)
            }
            
            index = smallerChildIndex
        }
    }
    
    size() {
        return this.heap.length
    }
}

function solution(jobs) {
    let len = jobs.length
    
    let heap = new Heap()
    
    jobs.sort((a, b) => a[0]-b[0])
    
    let time = 0
    let complete = 0
    let total = 0
    
    while (jobs.length || heap.size()) {
        while (jobs.length) {
            if (jobs[0][0] === time) {
                heap.heappush(jobs.shift())
            } else {
                break
            }
        }
        
        if (heap.size() && time >= complete) {
            const task = heap.heappop()
            complete = time + task[1]
            total += complete - task[0]
        }
        time++
    }
    
    return Math.floor(total / len);
}