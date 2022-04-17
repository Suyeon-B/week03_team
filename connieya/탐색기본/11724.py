import sys
N, M = map(int, sys.stdin.readline().split())
sys.setrecursionlimit(10**6)
ans = 0
graph = [[ ] for _ in range(N+1)]
visited = [False]*(N+1)

def dfs(start):
    visited[start] = True
    for nxt in graph[start]:
        if visited[nxt] == False:
            dfs(nxt)


for i in range(M):
    a ,b  = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(1,N+1):
    if visited[i] == False:
        dfs(i)
        ans += 1

print(ans)

