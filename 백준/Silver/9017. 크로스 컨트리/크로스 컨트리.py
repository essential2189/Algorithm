def solution(team_list):
    team_dict = {}

    # 각 팀의 참가 선수가 몇명인지
    for i in team_list:
        if i not in team_dict:
            team_dict[i] = 1
        else:
            team_dict[i] += 1

    # 참가 선수 6명 이하의 팀 listing
    na = []
    for k, v in team_dict.items():
        if v < 6:
            na.append(k)

    team_dict = {}
    team_member_count = {}
    score = 1

    # 참가 선수 6명 이상의 각 팀의 점수 계산
    for l in team_list:
        if l not in na:
            if l not in team_member_count:
                team_member_count[l] = 1

            if team_member_count[l] < 4:
                if l not in team_dict:
                    team_dict[l] = score
                else:
                    team_dict[l] += score
                    team_member_count[l] += 1

            score += 1


    team_dict_sort = sorted(team_dict.items(), key=lambda i:i[1])
    win_team = team_dict_sort[0][0]
    max_score = team_dict_sort[0][1]
    same_team = set()

    # 같은 점수인 팀이 있는지 확인
    for i in range(len(team_dict_sort)-1):
        if team_dict_sort[i][1] == team_dict_sort[i+1][1] and max_score == team_dict_sort[i][1]:
            same_team.add(team_dict_sort[i][0])
            same_team.add(team_dict_sort[i+1][0])

    # 같은 점수인 팀이 있을 경우 먼저 5번째 주자가 들어오는 팀 찾기
    if len(same_team) > 1:
        count_five = {}
        for l in team_list:
            if l in same_team and l not in na:
                idx = team_list.index(l)
                team_list[idx] = -1
                if l not in count_five:
                    count_five[l] = 1
                else:
                    count_five[l] += 1
                if count_five[l] >= 5:
                    win_team = l
                    break

    return win_team

t = int(input())

for _ in range(t):
    n = int(input())
    list_ = list(map(int, input().split()))
    print(solution(list_))
