def solution(N):

    for i in range(1, N):
        str_i = str(i)
        three = str_i.count("3")
        six = str_i.count("6")
        nine = str_i.count("9")

        # 369 갯수당 - 표시
        if three > 0 or six > 0 or nine > 0:
            if three > 0:
                for _ in range(three):
                    print("-", end="")
            if six > 0:
                for _ in range(six):
                    print("-", end="")
            if nine > 0:
                for _ in range(nine):
                    print("-", end="")
            print(" ", end="")
        else:
            print(i, end=" ")

    if "3" in str(N) or "6" in str(N) or "9" in str(N):
        print("-", end="")
    else:
        print(N, end="")


solution(int(input()))