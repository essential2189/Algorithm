n, score, p = map(int, input().split())

score_list = []
if n:
    score_list = list(map(int, input().split()))
    score_list.append(score)
    score_list.sort(reverse=True)
    rank = score_list.index(score) + 1

    if rank > p:
        print(-1)
    else:
        if n == p and score == score_list[-1]:
            print(-1)
        else:
            print(rank)
else:
    print(1)

