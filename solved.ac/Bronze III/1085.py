def solution():
    x, y, w, h = map(int, input().split())

    temp = []


    temp.append(abs(w - x))
    temp.append(abs(x))
    temp.append(abs(h - y))
    temp.append(abs(y))

    return sorted(temp)[0]


answer = solution()
print(answer)