def solution():
    n = int(input())

    six = 666

    count = 0

    while True:
        if str(six).count("666") >= 1:
            six += 1
            count += 1
        else:
            six += 1

        if count == n:
            print(six-1)
            break


solution()