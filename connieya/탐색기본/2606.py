import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
ans = 0
visited = [False]*(N+1)
graph = [[] for _ in range(N+1)]

def dfs(start):
    visited[start] = True
    for nxt in graph[start]:
        if visited[nxt] == False:
            dfs(nxt)


for i in range(M):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(1)
for i in range(2,N+1):
    if visited[i] == True:
        ans+=1

print(ans)

