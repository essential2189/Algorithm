N, K = map(int, input().split())

country = []
for _ in range(N):
    country.append(list(map(int, input().split())))

country_dict = {}
for c in country:
    country_dict[c[0]] = c[1:]

country_dict = sorted(country_dict.items(), key=lambda item: item[1], reverse=True)

last = []
for idx, cd in enumerate(country_dict):
    if cd[0] == K:
        if last == cd[1:]:
            print(idx)
            break
        print(idx + 1)
        break
    last = cd[1:]
