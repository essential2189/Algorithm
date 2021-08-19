def solution(N, A, B):
    answer = 0
    a_s = sorted(A)
    max = B[0]
    for i in range(N):
        for k in range(N-1):
            if B[k] < B[k+1]:
                if B[k+1] > max:
                    max = B[k+1]

        b_index = B.index(max)
        answer += a_s[i] * B[b_index]
        B[b_index] = -1
        max = B[0]

    return answer

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = solution(N, A, B)
print(answer)