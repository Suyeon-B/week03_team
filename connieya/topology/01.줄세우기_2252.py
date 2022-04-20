import sys
from collections import deque

sys.stdin = open('input.txt')

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
indegree = [0]*(n+1)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] +=1


queue = deque()
for i in range(1,n+1):
    if indegree[i] == 0:
        queue.append(i)


while queue:
    now = queue.popleft()
    print(now , end= ' ')
    for next in graph[now]:
        indegree[next] -=1
        if indegree[next] == 0:
            queue.append(next)
