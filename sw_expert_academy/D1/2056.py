def solution():
    date = input()
    answer = ""

    _31 = [1, 3, 5, 7, 8, 10, 12]
    _30 = [4, 6, 9, 11]

    year = date[:4]
    month = date[4:6]
    day = date[6:]

    answer += year+"/"

    if 1 <= int(month) <= 12:
        answer += month + "/"
    else:
        return -1

    if int(month) in _31 and 1 <= int(day) <= 31:
        answer += day
    elif int(month) in _30 and 1 <= int(day) <= 30:
        answer += day
    elif int(month) == 2 and 1 <= int(day) <= 28:
        answer += day
    else:
        return -1

    return answer

for t in range(int(input())):
    answer = solution()

    print("#{} {}".format(t+1, answer))