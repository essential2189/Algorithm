n, m = map(int, input().split())

words = {}
for i in range(n):
    word = input()
    if len(word) >= m:
        if words.get(word):
            words[word][0] += 1
        else:
            words[word] = [1, len(word), word]

answer = sorted(words.items(), key=lambda x: (-x[1][0], -x[1][1], x[1][2]))

for a in answer:
    print(a[0])