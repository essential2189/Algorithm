def check(Q, row):
    for i in range(row): # row 전까지 range가 도니깐 row가 2면 0~1 row와 동일한 column 검색
        # i=0: 1 0 0 0 0
        # i=1: 1 0 0 0 0
        # i=2: 1 0 0 0 0

        # i는 row보다 작은 모든 수
        # Q[i] == Q[row] : 서로 같은 column에 있고
        # abs(Q[i] - Q[row]) == row - i : 대각선에 있을 때
        if Q[i] == Q[row] or abs(Q[i] - Q[row]) == row - i:
            return False

    return True


def dfs(Q, row):
    # Q[row(y)] = col(x)
    n = len(Q)
    count = 0

    if n == row:
        return 1

    for col in range(n):
        Q[row] = col    # 퀸 두기

        if check(Q, row):
            count += dfs(Q, row + 1)

    return count

def solution(n):
    return dfs([0] * n, 0)

for t in range(1, int(input())+1):
    count = solution(int(input()))

    print("#{} {}".format(t, count))