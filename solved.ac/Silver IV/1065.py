N = int(input())
answer = 0
if N >= 100:
    answer += 99
if N < 100:
    for k in range(int(N)):
        answer += 1

for i in range((N//10)+1):
    for j in range(10):
        if i*10+j > N:
            break
        if i//10 - i%10 == i%10 - j and i//10 != 0:
            answer += 1


print(answer)
