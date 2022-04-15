# 시간초과 -> visited 다르게 구현해서 시간복잡도 낮추기
import sys, collections
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = collections.defaultdict(list) # 빈 그래프 생성, default는 list
for i in range(1, m+1):
    vertex1, vertex2 = map(int, input().split())
    graph[vertex1] = sorted(graph[vertex1]+[vertex2])
    graph[vertex2] = sorted(graph[vertex2]+[vertex1]) # 무방향 그래프이므로

# recursive DFS
def DFS(start_v, visited=[]):
    visited.append(start_v)
    for v in graph[start_v]:
        if v not in visited:
            visited = DFS(v, visited)
    return visited

visited = DFS(1)
cnt = 1
for i in range(1, n+1):
    if i not in visited:
        visited = DFS(i)
        cnt+=1

print(cnt)