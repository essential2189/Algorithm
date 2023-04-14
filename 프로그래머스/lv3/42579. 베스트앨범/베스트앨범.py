def solution(genres, plays):
    answer = []
    dict_list = {}
    dict_count = {}
    
    for i in range(len(genres)):
        if genres[i] not in dict_list:
            dict_list[genres[i]] = [[plays[i], i]]
            dict_count[genres[i]] = plays[i]
        else :
            dict_list[genres[i]].append([plays[i], i])
            dict_count[genres[i]] += plays[i]
    
    
    for k, v in sorted(dict_count.items(), key=lambda x: x[1], reverse=True):
        for h, i in sorted(dict_list[k], key=lambda x: (-x[0], x[1]))[:2]:
            answer.append(i)
        
    return answer