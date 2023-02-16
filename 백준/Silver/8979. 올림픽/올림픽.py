N, K = map(int, input().split())

country_list = []
for _ in range(N):
    country_list.append(list(map(int, input().split())))

country_list.sort(key = lambda x : (x[1], x[2], x[3]), reverse=True)

for i in range(N):
    if country_list[i][0] == K:
        index = i

for i in range(N):
    if country_list[index][1:] == country_list[i][1:]:
        print(i + 1)
        break