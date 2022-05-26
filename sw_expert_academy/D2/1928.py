

Base64 = {s: i for i, s in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")}

def solution():
    answer = ""
    s = input()

    bin_ = ""
    for i in s:
        sextets = Base64[i]
        bin_sextets = bin(sextets)[2:]
        zero = ""
        for _ in range(6 - len(bin_sextets)):
            zero += "0"

        bin_ += str(zero+bin_sextets)


    for i in range(0, len(bin_), 8):
        answer += chr(int(bin_[i:i+8], 2))

    return answer



for t in range(1, int(input())+1):
    answer = solution()

    print("#{} {}".format(t, answer))