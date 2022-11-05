def solution(n):
    A, B, C = map(int, n.split(" "))

    result1 = (A + B) % C
    result2 = ((A % C) + (B % C)) % C
    result3 = (A * B) % C
    result4 = ((A % C) * (B % C)) % C

    return [result1, result2, result3, result4]


for i in solution(input()):
    print(i)