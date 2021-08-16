# 0과 1의 횟수만 출력하면 되기 때문에 법칙성을 만들어주기 위해 0~2까지의 0과 1의 횟수를 리스트로 만든다.
zero = [1, 0, 1]
one = [0, 1, 1]

# arr_num = 0  1  2
#   zero = [1, 0, 1]
#    one = [0, 1, 1]
# 이렇게 만들어주고 만약 4가 들어오면
# 먼저 3을 실행한다. (arr_num 1과 2를 더함)
# arr_num = 0  1  2  3
#   zero = [1, 0, 1, 0+1]
#    one = [0, 1, 1, 1+1]
# 다음에 4를 실행한다. (arr_num 2와 3을 더함)
# arr_num = 0  1  2  3  4
#   zero = [1, 0, 1, 1, 1+1]
#    one = [0, 1, 1, 2, 1+2]
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
