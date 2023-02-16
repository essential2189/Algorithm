N, K = map(int, input().split())

country_list = []
for _ in range(N):
    country_list.append(list(map(int, input().split())))

country_dict = {}
for c in country_list:
    if str(c[1:]) not in country_dict:
        country_dict[str(c[1:])] = []
    country_dict[str(c[1:])].append(c[0])

country_dict = sorted(country_dict.items(), key=lambda item: list(item[0]), reverse=True)

def solution():
    for idx, cd in enumerate(country_dict):
        for country in cd[1]:
            if country == K:
                return idx+1

print(solution())
