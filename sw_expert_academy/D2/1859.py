from collections import deque

def solution():
    buy = []
    total = 0
    N = int(input())
    num = input().split(" ")

    num_list = [int(i) for i in num]
    q = deque(num_list)
    max_ = max(q)

    while q:
        num = q.popleft()
        # 가장 큰 값까지 무조건 더해서 가장 큰값에 팔기
        if num < max_:
            buy.append(num)
        elif num == max_:
            while buy:
                b = buy.pop()
                total += num - b
            # 가장 큰 값에 팔았으면 남은거 중에서 가장 큰 값 설정해서 그 값에 팔기
            if q:
                max_ = max(q)

    return total

for m in range(int(input())):
    total = solution()

    print("#{} {}".format(m+1, total))