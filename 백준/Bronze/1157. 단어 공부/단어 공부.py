

def solution(string):
    if len(string) == 1:
        return string

    dict = {}

    for s in string:
        if s not in dict:
            dict[s] = 1
        else:
            dict[s] = dict[s] + 1

    sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)

    if sorted_dict[0][1] == sorted_dict[1][1]:
        return "?"
    else:
        return sorted_dict[0][0]

string = input().upper()
print(solution(string))