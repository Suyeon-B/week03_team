import sys, collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = collections.defaultdict(list) # 빈 그래프 생성, default는 list
for i in range(1, n):
    vertex1, vertex2 = map(int, input().split())
    graph[vertex1] += [vertex2]
    graph[vertex2] += [vertex1]

# recursive DFS
visited = [False] * (n+1)
parent = collections.defaultdict(int)
def DFS(start_node):
    visited[start_node] = True
    for v in graph[start_node]:
        if not visited[v]:
            parent[v] = start_node
            DFS(v)

DFS(1)
for i in range(2, n+1):
    print(parent[i])