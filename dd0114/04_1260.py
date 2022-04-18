# Depth First search
import heapq
import queue
import sys
from collections import deque

input= sys.stdin.readline

def dfs(n):
    print(n, end= ' ')
    visited[n] = True
    for i in graph[n]:
        if not visited[i]:
            dfs(i)
# 받은 수를 찍는다.
# 받은 곳을 방문으로 전환
# 연결된 노드들을 for문으로 불러온다.
# 방분 하지 않은 곳이라면.
# 다시 dfs를 재귀() 

def bfs(n):
    visited[n]= True
    queue = deque([n])
    while queue :
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                # heapq.heappush(queue, i)
                visited[i] = True

# 받은 곳을 방문으로 바꾼다
# 큐를 만든다.
# 큐에 연결 노드를 넣고 포문으로 돌리는 식 
# 큐에서 빠져나오면서 찍히도록
# while 큐. -> 큐에서 팝레프트. -> 프린트 포문으로 순차적으로 큐에 넣는다.
# 넣으면서느 프린트 안찍힘. pop레프트 되면서 찍히도록 작동


n, m, v = map(int,input().split())

graph = [[]for _ in range(n+1)]

visited = [False]*(n+1)

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    graph[i].sort()
# 소팅해주는 이유는??
bfs(1)

