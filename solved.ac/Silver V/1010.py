def fac(f):
    fac = 1
    for i in range(1, f+1):
        fac *= i

    return fac

def nCr(N, M):
    if M >= N:
        return fac(M) / (fac(N) * fac(M-N))

    elif M < N:
        return fac(N) / (fac(M) * fac(N-M))

T = int(input())

for t in range(T):
    N, M = input().split()
    N = int(N)
    M = int(M)
    answer = nCr(N, M)
    print(int(answer))
