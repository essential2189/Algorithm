def solution(sizes):
    s_sizes = []
    
    for s in sizes:
        s_sizes.append(sorted(s, reverse=True))
    
    x = max(s_sizes, key=lambda i:i[0])[0]
    y = max(s_sizes, key=lambda i:i[1])[1]
    
    return x * y