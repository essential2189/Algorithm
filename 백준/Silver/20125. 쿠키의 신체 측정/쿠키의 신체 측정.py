def solution(cookie):
    flag = False
    for i in range(len(cookie)):
        for j in range(len(cookie[0])):
            if cookie[i][j] == "*":
                head_location = [i, j]
                flag = True
                break
        if flag:
            break

    heart_location = [head_location[0] + 1, head_location[1]]

    left_hand = cookie[heart_location[0]][:heart_location[1]]
    right_hand = cookie[heart_location[0]][heart_location[1]+1:]

    left_hand_count = left_hand.count("*")
    right_hand_count = right_hand.count("*")

    body_count = 0
    right_foot_count = 0
    left_foot_count = 0
    for c in cookie[heart_location[0] + 1:]:
        if c[heart_location[1]] == "*":
            body_count += 1
        else:
            if c[heart_location[1] - 1] == "*":
                left_foot_count += 1
            if c[heart_location[1] + 1] == "*":
                right_foot_count += 1

    return "{0} {1}\n{2} {3} {4} {5} {6}".format(heart_location[0]+1, heart_location[1]+1, left_hand_count, right_hand_count, body_count, left_foot_count, right_foot_count)



n = int(input())
cookie = []
for _ in range(n):
    cookie.append(input())

print(solution(cookie))