s = sorted(list(map(int, list(input()))))

i = s.index(1)

answer = ''
for _ in range(i // 2):
    answer += '0'

for _ in range(len(s[i:]) // 2):
    answer += '1'

print(answer)