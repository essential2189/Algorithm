t = int(input())

for _ in range(t):
    n, k, t, m = list(map(int, input().split(" ")))

    # { 팀: [ 최종 점수, 제출 횟수, 제출 시간 ] }
    record = {x:[0, 0, 0] for x in range(1, n+1)}
    # { 팀: [ 각 문제들에 대한 제출 점수 ] }
    score = {x:[0] * (k + 1) for x in range(1, n+1)}

    for time in range(1, m+1):
        i, j, s = map(int, input().split(" "))

        if score[i][j] < s:
            score[i][j] = s
            record[i][0] = sum(score[i])
        
        record[i][1] += 1
        record[i][2] = time
    
    results = list(record.items())
    results.sort(key=lambda x: (-x[1][0], x[1][1], x[1][2]))

    for i in range(len(results)):
        if results[i][0] == t:
            print(i + 1)