import sys

M = int(input())
S = set()
for i in range(M):
    cal = sys.stdin.readline().strip().split()

    if len(cal) == 1:
        if cal[0] == 'all':
            S = set([k for k in range(1, 21)])
        elif cal[0] == 'empty':
            S = set()

    else:
        num = int(cal[1])
        if cal[0] == 'add':
            S.add(num)
        elif cal[0] == 'remove':
            S.discard(num)
        elif cal[0] == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif cal[0] == 'toggle':
            if num in S:
                S.discard(num)
            else:
                S.add(num)