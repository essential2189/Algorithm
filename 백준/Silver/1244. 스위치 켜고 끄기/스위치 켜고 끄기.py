def on_off_switch(num):
    global switch_list
    if switch_list[num] == 1:
        switch_list[num] = 0
    elif switch_list[num] == 0:
        switch_list[num] = 1

n = int(input())

switch_list = list(map(int, input().split()))

student = int(input())

for _ in range(student):
    gender, num = map(int, input().split())

    if gender == 1:
        for i in range(n):
            if (i + 1) % num == 0:
                on_off_switch(i)

    elif gender == 2:
        for i in range(n):
            if num-1 - i - 1 >= 0 and num-1 + i + 1 < n:
                if switch_list[num-1 - i - 1] != switch_list[num-1 + i + 1]:
                    break

                on_off_switch(num-1 - i - 1)
                on_off_switch(num-1 + i + 1)

        on_off_switch(num-1)


for i in range(0, n, 20):
    print(" ".join(map(str, switch_list[i:i+20])))