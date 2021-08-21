def solution(p, o, N):
    answer = 0
    p = sorted(p)
    o = sorted(o)
    six = N // 6
    one = N % 6
    if p[0] <= o[0]*6 :     # 1패키지 가격이 낱개 6개보다 쌀때
        if one*o[0] <= p[0]:        # 남은거 낱개로 산게 1패키지로 살때보다 쌀때 (낱개 갯수 * 낱개 가격 <= 1패키지 가격)
            answer = (six*p[0] + one*o[0])
        elif one*o[0] > p[0]:       # 남은거 낱개로 산게 1패키지로 살때보다 비쌀때 (차라리 1패키지 하나 더 사는게 이득일때)
            answer = (six+1)*p[0]
    else :                  # 1패키지 가격이 낱개 6개보다 비쌀때
        answer = o[0]*N

    return answer

N, M = map(int, input().split())
p = [0] * M
o = [0] * M
for i in range(M):
    p[i], o[i] = list(map(int, input().split()))

answer = solution(p, o, N)
print(answer)
