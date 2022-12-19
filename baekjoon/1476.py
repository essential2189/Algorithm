def solution():
    E, S, M = map(int, input().split(" "))

    count, E_count, S_count, M_count = 0, 0, 0, 0

    while True:
        count += 1
        E_count += 1
        S_count += 1
        M_count += 1

        if E_count > 15:
            E_count = 1
        if S_count > 28:
            S_count = 1
        if M_count > 19:
            M_count = 1

        if E == E_count and S_count == S and M_count == M:
            return count

print(solution())
