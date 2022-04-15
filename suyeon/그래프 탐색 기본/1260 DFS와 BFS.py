import sys, collections
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())

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

# deque 이용 BFS
def BFS(start_v):
    DQ = deque()
    visited = [start_v]
    DQ.append(start_v)
    while DQ:
        v = DQ.popleft()
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                DQ.append(w)
    return visited
    

print(" ".join(map(str, DFS(v))))
print(" ".join(map(str, BFS(v))))