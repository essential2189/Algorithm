n, k = map(int, input().split())

table = list(input())

count = 0
for t in range(n):
    if table[t] == "P":
        for i in range(t-k, t+k+1):
            if n > i >= 0 and table[i] == "H":
                table[i] = "0"
                count += 1
                break

print(count)
