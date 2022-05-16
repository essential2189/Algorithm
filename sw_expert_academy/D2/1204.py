from sys import stdin
from collections import Counter

def solution():
    T = int(input())

    for _ in range(T):
        tc_num = int(input())
        score = stdin.readline().split(" ")
        score_int = [int(i) for i in score[0:-1]]
        counter = Counter(score_int).most_common(1)

        print("#{} {}".format(tc_num, counter[0][0]))



solution()