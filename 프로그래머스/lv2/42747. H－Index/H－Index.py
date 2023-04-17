def solution(citations):
    citations = sorted(citations)
    h = citations[-1]

    while True:
        count = 0
        for c in citations:
            if c >= h:
                count += 1
        if count >= h:
            return h
        h -= 1

    return h