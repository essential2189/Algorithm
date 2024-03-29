from collections import deque, defaultdict
from itertools import combinations

# 연결된 구역을 탐색하고, 해당 구역의 인구수와 연결된 구역 갯수를 계산하여 return한다.
def bfs(people, graph, same):
    start = same[0]
    visited = {start}
    q = deque([start])
    p_sum = 0

    while q:
        i = q.popleft()
        p_sum += people[i]

        for node in graph[i]:
            if node not in visited and node in same:
                q.append(node)
                visited.add(node)

    return p_sum, len(visited)

def solution(n, people, area):
    graph = defaultdict(list)
    result = float("inf")

    for i in range(n):
        for a in area[i][1:]:
            graph[i].append(a - 1)  # 구역이 1번부터 시작하기에 0부터 시작하게끔

    for i in range(1, n // 2 + 1):
        combis = list(combinations(range(n), i))    # 조합을 사용하여 구역을 나눈다. 이때 n의 절반(0~n // 2)만큼만 조합을 구하면 된다. 이는 mCn = n - mCn이 성립하는 조합의 성질을 잘 생각해보면 알 수 있다. 즉, 한 선거구에 m개의 구역을 할당하면, 다른 선거구에 n-m개의 구역이 자동적으로 할당된다.
        for combi in combis:
            people_sum1, count_area1 = bfs(people, graph, combi)     # 1구역의 인구수와 구역 갯수
            people_sum2, count_area2 = bfs(people, graph, [i for i in range(n) if i not in combi])     # 남은 2구역의 인구수와 구역 갯수

            if count_area1 + count_area2 == n:   # 1구역과 2구역의 구역 갯수의 합이 n과 같은지 검증
                result = min(result, abs(people_sum1 - people_sum2))

    if result == float("inf"):
        return -1

    return result


n = int(input())
people = list(map(int, input().split()))
area = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, people, area))