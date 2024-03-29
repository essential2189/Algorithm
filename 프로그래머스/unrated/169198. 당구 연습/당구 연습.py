import math

def distance(x1, y1, x2, y2):
    return (x1-x2)**2 + (y1-y2)**2


def solution(m, n, startX, startY, balls):
    answer = []
    
    for b in balls:
        dists = []
        
        # 위쪽 쿠션
        # 단, x좌표가 같고 목표의 y가 더 크면 안된다. (위쪽 따당)
        if not (b[0] == startX and b[1] > startY):
            d = distance(startX, startY, b[0], 2 * n - b[1])
            dists.append(d)
            
        # 아래쪽 쿠션
        # 단, x좌표가 같고 목표의 y가 더 작으면 안된다. (아레쪽 따당)
        if not (b[0] == startX and b[1] < startY):
            d = distance(startX, startY, b[0], -b[1])
            dists.append(d)
            
        # 왼쪽 쿠션
        # 단, y좌표가 같고 목표의 x가 더 작으면 안된다. (왼쪽 따당)
        if not (b[1] == startY and b[0] < startX):
            d = distance(startX, startY, -b[0], b[1])
            dists.append(d)
            
        # 오른쪽 쿠션
        # 단, y좌표가 같고 목표의 x가 더 크면 안된다. (오른쪽 따당)
        if not (b[1] == startY and b[0] > startX):
            d = distance(startX, startY, 2 * m - b[0], b[1])
            dists.append(d)
        
        answer.append(min(dists))
        
    return answer