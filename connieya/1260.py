import sys
N, M, V = map(int, sys.stdin.readline().split())
sys.setrecursionlimit(10**6)
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]
res = []


def dfs(start):
    visited[start] = True
    res.append(start)
    for next in graph[start]:
        if visited[next] == False:
            visited[next] = True
            dfs(next)

def bfs(start):
    res.clear()
    visited = [False]*(N+1)
    res.append(start)
    visited[start] = True
    queue = [start]
    while queue:
        start = queue.pop(0)
        for next in graph[start]:
            if visited[next] == False:
                visited[next] = True
                res.append(next)
                queue.append(next)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort()

dfs(V)
print(*res)
bfs(V)
print(*res)
