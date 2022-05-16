def dfs(count):
    global answer

    if not count:
        temp = int("".join(num_list))
        if temp > answer:
            answer = temp
        return

    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            num_list[i], num_list[j] = num_list[j], num_list[i]

            sum_ = "".join(num_list)
            if visited.get((sum_, count-1), 1):
                visited[(sum_, count-1)] = 0
                dfs(count-1)

            num_list[i], num_list[j] = num_list[j], num_list[i]




for N in range(int(input())):
    answer = -1
    num, m, = input().split(" ")

    num_list = list(num)
    m = int(m)

    visited = {}

    dfs(m)
    print("#"+str(N+1)+" "+str(answer))