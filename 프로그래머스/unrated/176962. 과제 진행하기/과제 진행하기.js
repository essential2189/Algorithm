function toMinute(time){
    let [h, m] = time.split(":")
    return Number(h) * 60 + Number(m)
}


function solution(plans) {
    var answer = [];
    
    let plansSort = plans.map((p) => [p[0], toMinute(p[1]), Number(p[2])]).sort((a, b) => a[1] - b[1])
    plansSort.push(["END", 1440, 1440])
    
    let wait = []

    for (let i = 0; i < plansSort.length - 1; i++) {
        let [lecture, startTime, time] = plansSort[i]
        let [nextLecture, nextStartTime, nextTime] = plansSort[i+1]
        
        let freeLeftTime = nextStartTime - startTime - time
        
        if(freeLeftTime >= 0) {
            answer.push(lecture)
            
            while (freeLeftTime && wait.length) {
                if (wait[wait.length-1][1] > freeLeftTime) {
                    wait[wait.length-1][1] -= freeLeftTime
                    freeLeftTime = 0
                } else {
                    answer.push(wait[wait.length-1][0])
                    freeLeftTime -= wait.pop()[1]
                }
            }
        } else {
            wait.push([lecture, Math.abs(freeLeftTime)])
        }
    }
    
    while (wait.length) {
        answer.push(wait.pop()[0])
    }

    return answer;
}