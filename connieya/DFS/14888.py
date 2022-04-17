import sys


def dfs(sum, L, N):
    global max, min
    if L == N:
        if sum > max:
            max = sum
        if sum < min:
            min = sum
        return

    if op[0] > 0:
        op[0] -= 1
        dfs(sum + number[L], L + 1, N)
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        dfs(sum - number[L], L + 1, N)
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        dfs(sum * number[L], L + 1, N)
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        if sum >= 0:
            dfs(sum // number[L], L + 1, N)
        else:
            sum *= -1
            sum //= number[L];
            dfs(-1*sum,L+1,N)
        op[3] += 1


N = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
max = -1e9 + 1
min = 1e9 + 1
dfs(number[0], 1, N)
print(max)
print(min)
