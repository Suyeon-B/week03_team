import sys
N = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())
ans = []

def DFS(sum, L, add, sub, mul, div):
    if L == N:
        ans.append(sum)
        return
    if add != 0: DFS(sum + number[L], L + 1, add - 1, sub, mul, div)
    if sub != 0: DFS(sum - number[L], L + 1, add, sub - 1, mul, div)
    if mul != 0: DFS(sum * number[L], L + 1, add, sub, mul - 1, div)
    if div != 0: DFS(int(sum / number[L]), L + 1, add, sub, mul, div - 1)



DFS(number[0], 1, add, sub, mul, div)
print(max(ans))
print(min(ans))
