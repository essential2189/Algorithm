

function solution(fees, records) {
    var answer = [];
    let object = {}
    let time_object = {}
    let in_object = {}
    const last_time = 23 * 60 + 59
    
    for (const r of records) {
        let r_split = r.split(" ")
        let time = r_split[0]
        let num = r_split[1]
        let status = r_split[2]
        
        let time_split = time.split(":")
        let minute = Number(time_split[0]) * 60 + Number(time_split[1])
        
        if (num.toString() in object) {
            object[num.toString()].push(minute)
        }else{
            object[num.toString()] = [minute]
        }
        
        if (num.toString() in in_object === false) {
            in_object[num.toString()] = 1
        }

        if (status === "OUT"){
            let minutes = object[num.toString()]
            let t = minutes[1] - minutes[0]
            
            if (num.toString() in time_object) {
                time_object[num.toString()] += t
            } else{
                time_object[num.toString()] = t
            }
            
            delete object[num.toString()]
            delete in_object[num.toString()]
        }
        
    }
    
    for (const key in in_object){
        if (key in time_object) {
            time_object[key] += last_time - object[key][object[key].length - 1]
        } else {
            time_object[key] = last_time - object[key][object[key].length - 1]
        }
    }
    
    time_object_sort = Object.keys(time_object)
    .sort()
    
    for (const key of time_object_sort){
        let money = 0
        if (time_object[key] <= fees[0]){
            answer.push(fees[1])
        } else{
            money += fees[1]
            money += Math.ceil((time_object[key] - fees[0]) / fees[2]) * fees[3]
            answer.push(money)
        }
    }
    
    return answer;
}