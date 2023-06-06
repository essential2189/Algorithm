import heapq

def solution(book_time):
    answer = 0
    
    book_minute = []
    for b in book_time:
        s, e = b
        sh, sm = list(map(int, s.split(":")))
        eh, em = list(map(int, e.split(":")))
        
        book_minute.append([sh*60+sm, eh*60+em])        
    
    book_minute.sort()
    
    room = [[book_minute[0]]]
    
    for i in range(1, len(book_minute)):
        flag = False
        for r in range(len(room)):
            if book_minute[i][0] >= room[r][-1][1] + 10:
                room[r].append(book_minute[i])
                flag = False
                break
            else:
                flag = True
                
        if flag:
            room.append([book_minute[i]])
            
                
    return len(room)