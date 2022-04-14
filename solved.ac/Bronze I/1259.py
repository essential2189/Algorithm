import sys


def solution():
    while True:
        str = sys.stdin.readline().strip()
        if str == "0":
            break
        str_int = []
        str_int_r = []

        if len(str) % 2 != 0:
            for i in range(len(str)//2):
                str_int.append(int(str[i]))

            for j in range(len(str)-1, len(str)//2, -1):
                str_int_r.append(int(str[j]))
        else:
            for i in range(len(str) // 2):
                str_int.append(int(str[i]))

            for j in range(len(str) - 1, len(str) // 2-1, -1):
                str_int_r.append(int(str[j]))

        if str_int == str_int_r:
            print("yes")
        else:
            print("no")



solution()
