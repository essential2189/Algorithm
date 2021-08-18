def solution(N, M, a):
    P = [p for p in range(1 , N+1)]
    answer = 0
    for i in range(M):
        p_len = len(P)
        p_index = P.index(a[i])
        if p_len - p_index > p_index:
            while 1:
                if a[i] == P[0]:        # 일치 P[0] pop
                    del P[0]
                    break
                else:                   # 수열 앞으로 회전 1 2 3 -> 2 3 1
                    P.append(P[0])
                    del P[0]
                    answer += 1
        else:
            while 1:
                if a[i] == P[0] :       # 일치 P[0] pop
                    del P[0]
                    break
                else:
                    P.insert(0, P[-1])  # 수열 뒤로 회전 1 2 3 -> 3 1 2
                    del P[-1]
                    answer += 1

    return answer

N = input().split()
N, M = map(int, N)

a = input().split()
a = list(map(int, a))
answer = solution(N, M, a)
print(answer)


