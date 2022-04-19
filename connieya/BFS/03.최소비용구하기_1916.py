import sys
import heapq
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]
INF = int(1e9)
for i in range(M):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((b,c))

start , end = map(int,sys.stdin.readline().split())

d = [INF]*(N+1)
d[start] = 0
q = []
heapq.heappush(q,(0,start))
while q:
    cost, now = heapq.heappop(q)
    if d[now] < cost: continue

    for nxt in graph[now]:
        next_cost = cost + nxt[1]
        if d[nxt[0]] > next_cost:
            d[nxt[0]] = next_cost
            heapq.heappush(q,(next_cost,nxt[0]))


print(d[end])
