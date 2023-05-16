def solution(n, l, w, h):
    start = 0
    end = max(l, w, h)

    for _ in range(1000):
        median = (start + end) / 2
        count = (l // median) * (w // median) * (h // median)

        if count >= n:
            start = median
        else:
            end = median

    print("%.10f" %(end))


n, l, w, h = list(map(int, input().split()))
solution(n, l, w, h)