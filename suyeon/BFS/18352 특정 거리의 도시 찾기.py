import sys, collections
from collections import deque
sys.stdin = open("BFS/input.txt",'r')
input = sys.stdin.readline

# 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
n, m, k, x = map(int, input().strip().split())

# graph 초기화
graph = collections.defaultdict(list)
for i in range(m):
    vertex1, vertex2 = map(int, input().strip().split())
    graph[vertex1] += [vertex2] # 단방향 그래프
visited = [False] * (n+1)
distances = collections.defaultdict(int)

# BFS
def bfs(start_v):
    visited[start_v] = True
    q = deque([[0, start_v]])
    cnt = 1
    while q:
        temp = q.popleft()
        v = temp[1]
        for w in graph[v]:
            if not visited[w]:
                cnt = distances[v]+1
                visited[w] = True
                q.append([cnt, w])
                distances[w] = cnt # start_v -> w 까지의 거리

result = []
bfs(x)
for i in range(1, n+1):
    dist = distances[i]
    if dist == k:
        result.append(i)
if len(result) == 0:
    print(-1)
else:
    result.sort()
    for i in range(len(result)):
        print(result[i])