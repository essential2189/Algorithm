def solution(r1, c1, r2, c2):
    directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]   # left, up, right, down
    board = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]

    max_board = (c2 - c1 + 1) * (r2 - r1 + 1)

    x = 0
    y = 0
    curr_direction_count = 0            # 한 방향에서 움직인 횟수
    need_to_change_direction_count = 1  # 한 방향에서 움직여야할 횟수
    num = 1
    curr_direction = 0                  # 움직여야할 방향

    while max_board > 0:
        if r1 <= y <= r2 and c1 <= x <= c2:
            board[y - r1][x - c1] = num
            max_board -= 1
            max_len = len(str(num))

        num += 1                    # 현재 소용돌이 숫자
        curr_direction_count += 1   # 현재 방향에서 움직인 횟수

        # 현재 방향으로 1칸씩 전진
        x += directions[curr_direction][0]
        y += directions[curr_direction][1]

        if curr_direction_count == need_to_change_direction_count:
            curr_direction_count = 0
            curr_direction = (curr_direction + 1) % 4       # 방향 전환, 총 4개의 방향이 순서대로 나오겠금
            if curr_direction == 0 or curr_direction == 2:  # 소용돌이를 그릴 때 왼쪽 또는 오른쪽으로 방향을 전환할 때마다 1칸씩 더 가야하는 패턴이 있다
                need_to_change_direction_count += 1


    for i in range(r2 - r1 + 1):
        for j in range(c2 - c1 + 1):
            print(str(board[i][j]).rjust(max_len), end=" ")     # rjust : 문자열을 오른쪽으로 지정된 숫자만큼 공백으로 정렬
        print()


r1, c1, r2, c2 = list(map(int, input().split()))
solution(r1, c1, r2, c2)
