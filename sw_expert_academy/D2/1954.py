def solution():
    N = int(input())

    snail = [[0]*N for _ in range(N)]
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    y = 0
    x = 0
    dist = 0

    for n in range(1, N*N + 1):
        snail[y][x] = n

        y += dir[dist][0]
        x += dir[dist][1]

        if 0 > y or 0 > x or N <= y or N <= x or snail[y][x] != 0:

            y -= dir[dist][0]
            x -= dir[dist][1]

            dist = (dist + 1) % 4

            y += dir[dist][0]
            x += dir[dist][1]

    return snail



for m in range(int(input())):
    snail = solution()

    print("#"+str(m+1))
    for s in snail:
        print(*s)
