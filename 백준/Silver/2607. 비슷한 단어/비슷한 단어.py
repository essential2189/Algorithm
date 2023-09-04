n = int(input())

target = list(input())

answer = 0

for _ in range(n-1):
    temp = target[:]
    word = input()
    count = 0

    for w in word:
        if w in temp:
            temp.remove(w)
        else:
            count += 1
    
    if count < 2 and len(temp) < 2:
        answer += 1

print(answer)
    