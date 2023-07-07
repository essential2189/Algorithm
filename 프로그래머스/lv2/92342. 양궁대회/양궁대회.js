function solution(n, info) {
    let answer
    let ryan = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    let maxDiff = 0
    
    
    // arrow: 현재까지 쏜 화살 수, idx: 현재 비교하고 있는 과녁 점수 index(0~10), ryan: 라이언의 점수표
    function dfs(peachScore, ryanScore, arrow, idx, ryan) {
        // 화살을 n만큼 쐇으면 멈춘다
        if (n < arrow) return
        
        // 10점까지 다 파악이 되면 차이를 구한다
        if (idx > 10) {
            let scoreDiff = ryanScore - peachScore
            
            if (maxDiff < scoreDiff) {
                ryan[10] = n - arrow // 남은 화살이 있다면 전부 0에 쏜다 (가장 낮은 점수를 더 많이 맞힌 경우를 return 해주세요)
                maxDiff = scoreDiff
                answer = ryan
            }
            return
        }
        
        // n발의 화살을 다 쏠 때 까지 ryan 점수 구하기
        if (n > arrow) {
            let candidate = [...ryan]
            let needShotArror = info[10 - idx] + 1 // 현재 과녁(idx)에 peach보다 높은 점수를 따기 위한 화살 개수 (peach의 화살 개수 + 1)
            
            candidate[10 - idx] = needShotArror // 해당 과녁 점수에서 peach를 이기기 위해 화살 소비
            
            dfs(peachScore, ryanScore + idx, arrow + needShotArror, idx + 1, candidate)
        }
        
        // peach 점수 구하기
        if (info[10 - idx] > 0) {
            dfs(peachScore + idx, ryanScore, arrow, idx + 1, ryan)
        } else {
            dfs(peachScore, ryanScore, arrow, idx + 1, ryan)
        }
    }
    
    dfs(0, 0, 0, 0, ryan)
    
    if(maxDiff <= 0) return [-1]
    
    return answer;
}