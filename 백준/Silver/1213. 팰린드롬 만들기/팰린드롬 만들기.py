from collections import Counter

def solution(name):
    name = sorted(name)

    counter = Counter(name)

    cnt_odd = 0
    center = ""

    for i in counter:
        if counter[i] % 2 != 0:
            cnt_odd += 1
            center += i
            name.remove(i)

        if cnt_odd > 1:
            return "I'm Sorry Hansoo"

    answer = ""
    for i in range(0, len(name), 2):
        answer += name[i]

    return answer + center + answer[::-1]


print(solution(input()))
