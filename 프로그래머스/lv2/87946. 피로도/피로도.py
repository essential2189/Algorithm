from itertools import permutations

def solution(k, dungeons):
    answer = [0]
    
    per = list(permutations(dungeons, len(dungeons)))
    
    for p in per:
        temp = k
        count = 0
        for dungeon in p:
            if dungeon[0] <= temp:
                temp -= dungeon[1]
                count += 1
        answer.append(count)
        
    return max(answer)