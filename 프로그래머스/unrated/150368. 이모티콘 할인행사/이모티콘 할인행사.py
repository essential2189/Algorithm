def dfs(stack, combi_len):
    if len(stack) == combi_len:
        combi.append(stack[:])
        return
    
    for d in discount:
        stack.append(d)
        dfs(stack, combi_len)
        stack.pop()
            
    return


def solution(users, emoticons):
    global combi
    global discount

    combi = []
    discount = [10, 20, 30, 40]
    
    dfs([], len(emoticons))
    print(len(combi))
    
    answer = [0, 0]
    
    for d in combi:
        emoticon_plus = 0
        sell = 0
        for u in users:
            pay = 0
            user_disc, money = u

            for i in range(len(emoticons)):
                if d[i] >= user_disc:
                    pay += emoticons[i] * (1 - (d[i] / 100))
                    
                if pay >= money:
                    break
                
            if pay >= money:
                pay = 0
                emoticon_plus += 1
            sell += pay
            
        if emoticon_plus >= answer[0]:
            if emoticon_plus == answer[0]:
                answer[1] = max(answer[1], sell)
            else:
                answer[1] = sell
            answer[0] = emoticon_plus
            
    return answer