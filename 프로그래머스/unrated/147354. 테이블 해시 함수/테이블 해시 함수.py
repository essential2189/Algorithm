def solution(data, col, row_begin, row_end):
    data_sort = sorted(data, key=lambda x: (x[col-1], -x[0]))
    
    rows = data_sort[row_begin-1:row_end]
    
    row_num = [i for i in range(row_begin, row_end+1)]
    
    mod = []
    for i in range(len(rows)):
        temp = 0
        for r in rows[i]:
            temp += r % row_num[i]
        mod.append(temp)
    
    answer = mod[0]
    for m in mod[1:]:
        answer ^= m
    
    return answer