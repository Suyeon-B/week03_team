import sys
from collections import deque

sys.stdin = open('input.txt')
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

indegree = [0] * (n + 1)
outdegree = [0] * (n + 1)
result = []
elements = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    indegree[b] += 1
    outdegree[a] += 1

queue = deque()
for i in range(1, n + 1):
    if outdegree[i] == 0:
        result.append(i)

queue.append(n)
elements[n] = 1

while queue:
    now = queue.popleft()
    for next, count in graph[now]:
        elements[next] += elements[now] * count
        indegree[next]-=1
        if indegree[next] == 0:
            queue.append(next)

for r in result:
    print(r , elements[r])
