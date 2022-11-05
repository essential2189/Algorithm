def solution(n):

    flag = True
    m = ""
    while flag:
        m += "1"

        if int(m) % int(n) == 0:
            return len(m)



while True:
    try:
        print(solution(input()))
    except:
        break