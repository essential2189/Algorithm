def solution(h):
    for i in range(len(h)):
        for j in range(i+1, len(h)):
            temp = h[:]
            del temp[i]
            del temp[j-1]
            if sum(temp) == 100:
                return temp

h = []
for _ in range(9):
    h.append(int(input()))

result = solution(sorted(h))
for r in result:
    print(r)

