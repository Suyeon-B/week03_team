import sys
sys.setrecursionlimit(10 ** 6)
def dfs(start, prev):
    count = 0
    for next in graph[start]:
        if next == prev: continue
        if str[next - 1] == '1':
            count += 1
            continue
        checked[next] = True
        count += dfs(next, start)

    return count

N = int(sys.stdin.readline())
str = sys.stdin.readline()
graph = [[] for _ in range(N + 1)]
checked = [False] * (N + 1)
ans = 0

for i in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    if str[i - 1] == '0' and not checked[i]:
        checked[i] = True
        c = dfs(i, i)
        ans += c * (c - 1)

cnt = 0
for i in range(1, N + 1):
    if str[i - 1] == '1':
        for next in graph[i]:
            if str[next - 1] == '1':
                cnt += 1

print(ans + cnt)
