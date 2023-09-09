import sys
import heapq

input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    numbers = map(int, input().split())
    for number in numbers:
        if len(heap) < n: # heap의 크기를 n개로 유지
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])

