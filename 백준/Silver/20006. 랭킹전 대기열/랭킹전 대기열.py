import sys

input = sys.stdin.readline

p, m = map(int, input().strip().split(" "))

# [i, [...]]
room = []
for _ in range(p):
    level, nickname = input().strip().split(" ")
    level = int(level)

    need_new_room = True
    for i in range(len(room)):
        if len(room[i][1]) == m:
            continue
            
        l, name_list = room[i]    
        if l - 10 <= level <= l + 10:
            room[i][1].append([level, nickname])
            need_new_room = False
            break

    if need_new_room:
        room.append([level, [[level, nickname]]])
        
for i in range(len(room)):
    if len(room[i][1]) == m:
        print("Started!")
        
        room_sort = sorted(room[i][1], key=lambda x:x[1])
        for r in room_sort:
            print(r[0], r[1])
        
    else:
        print("Waiting!")
        
        room_sort = sorted(room[i][1], key=lambda x:x[1])
        for r in room_sort:
            print(r[0], r[1])