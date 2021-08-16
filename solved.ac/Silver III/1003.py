zero = [1, 0, 1]
one = [0, 1, 1]
def fibonacci(n) :
    l = len(zero)
    if n >= l:
        for i in range(l, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(zero[n], one[n])


T = int(input())
for i in range(T):
    n = int(input())
    fibonacci(n)
