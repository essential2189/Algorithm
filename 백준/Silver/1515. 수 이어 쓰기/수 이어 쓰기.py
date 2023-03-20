n = input()

count = 0
while True:
    count += 1
    count_str = str(count)
    while len(n) > 0 and len(count_str) > 0:
        if n[0] == count_str[0]:
            n = n[1:]
        count_str = count_str[1:]

    if len(n) == 0:
        print(count)
        break







