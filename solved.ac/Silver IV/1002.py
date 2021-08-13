def solution(x1, y1, r1, x2, y2, r2):
    dis = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

    # if 순서 중요
    # 두 원이 일치하는 경우
    if dis == 0 and r1 == r2 :
        answer = -1

    # 두 원이 한점에서 만나는 경우(내적, 외적)
    elif dis == r1+r2 or abs(r1-r2) == dis :
        answer = 1

    # 두 원이 두점에서 만나는 경우
    elif abs(r1-r2) < dis < r1+r2 :
        answer = 2

    # 두 원이 만나지 않는 경우
    else :
        answer = 0

    return answer

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = input().split()
    x1, y1, r1, x2, y2, r2 = int(x1), int(y1), int(r1), int(x2), int(y2), int(r2)
    answer = solution(x1, y1, r1, x2, y2, r2)
    print(answer)
