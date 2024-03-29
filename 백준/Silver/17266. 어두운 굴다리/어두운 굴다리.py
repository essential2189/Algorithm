def solution(n, m, lights):
    arr = [0 for _ in range(n+1)]

    for l in lights:
        arr[l] = 1

    first = 0
    for i in arr:
        if i == 0:
            first += 1
        else:
            break
    
    max_count = 0
    for i in range(len(lights)-1):
        temp = lights[i+1] - lights[i]
        
        if temp % 2 == 0:
            temp = temp // 2
        else:
            temp = temp // 2 + 1
        
        max_count = max(max_count, temp)
    
    last = n - lights[-1]

    return max(first, max_count, last)

n = int(input())
m = int(input())
lights = list(map(int, input().split()))

print(solution(n, m, lights))