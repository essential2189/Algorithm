def solution(n):
    score = input().split()

    int_score = [int(i) for i in score]

    int_score.sort()

    idx = len(int_score) // 2

    print(int_score[idx])


solution(int(input()))
