const count = (arr, word) => arr.filter(el => el === word).length

function solution(picks, minerals) {
    let pickMap = [{"diamond": 1, "iron": 1, "stone": 1},
                    {"diamond": 5, "iron": 1, "stone": 1},
                    {"diamond": 25, "iron": 5, "stone": 1},
                  ]
    
    minerals = minerals.slice(0, picks.reduce((a,c) => a + 5 * c, 0))

    let mineral = []
    for (let i = 0; i < minerals.length; i += 5) {
        mineral.push(minerals.slice(i, i+5))
    }
    
    mineral.sort((a, b) => {
        const aDiamondCnt = count(a, "diamond")
        const bDiamondCnt = count(b, "diamond")
        
        if (aDiamondCnt === bDiamondCnt) {
            const aIronCnt = count(a, "iron")
            const bIronCnt = count(b, "iron")
            
            return bIronCnt - aIronCnt
        }
        return bDiamondCnt - aDiamondCnt
    })
    
    let i = picks[0] ? 0 : picks[1] ? 1 : 2
    
    let tired = 0
    for (const m of mineral){
        tired += m.reduce((a, c) => a + pickMap[i][c], 0)
        if (--picks[i] <= 0) {
            i++
        }
        if (picks.every(el => !el)) {
            return tired
        }
    }
    
    return tired
}