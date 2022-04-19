def solution():
    T = 10


    for t in range(T):
        answer = 0
        N = int(input())
        B = input()
        B = B.split()

        for l in range(2, len(B) - 2):
            f1 = int(B[l]) - int(B[l+1])
            f2 = int(B[l]) - int(B[l+2])
            b1 = int(B[l]) - int(B[l-1])
            b2 = int(B[l]) - int(B[l-2])

            if f1 >= 1 and f2 >= 1 and b1 >= 1 and b2 >= 1:
                min_ = min(f1, f2, b1, b2)
                answer += min_

        print("#" + str(t+1) + " " + str(answer))



solution()