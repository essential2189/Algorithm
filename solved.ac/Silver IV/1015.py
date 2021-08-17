def solution(A, N):
    P = [0 for l in range(N)]
    a_s = sorted(A)
    dup_check = []
    num = 0
    for i in range(N):
        if a_s[i] in dup_check:
            continue
        for j in range(N):
            if a_s[i] == A[j]:
                P[j] = num
                num+=1
                dup_check.append(a_s[i])

    for k in range(N):
        print(P[k], end=' ')

N = int(input())

a = input().split()
a = list(map(int, a))
solution(a, N)









# def solution(A, N):
#     P = [0 for l in range(N)]
#     a_s = sorted(A)
#     dup_check = []
#     num = 0
#     for i in range(N):
#         if a_s[i] in dup_check:
#             continue
#         for j in range(N):
#             if a_s[i] == A[j]:
#                 P[j] = num
#         if a_s[i] not in dup_check:
#             num += 1
#         dup_check.append(a_s[i])
#     print(P)
#
# N = int(input())
#
# a = input().split()
# a = list(map(int, a))
# solution(a, N)