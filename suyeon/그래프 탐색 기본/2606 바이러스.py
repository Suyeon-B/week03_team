# visited를 미리 배열로 지정해주어 시간 복잡도 개선
import sys, collections
sys.setrecursionlimit(10**6) # python RecursionError 방지
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

graph = collections.defaultdict(list) # 빈 그래프 생성, default는 list
for i in range(1, m+1):
    vertex1, vertex2 = map(int, input().split())
    graph[vertex1] += [vertex2]
    graph[vertex2] += [vertex1] # 무방향 그래프이므로

# recursive DFS
visited = [False] * (n+1)
path = []
def DFS(start_v):
    path.append(start_v)
    visited[start_v] = True
    for v in graph[start_v]:
        if not visited[v]:
            DFS(v)

DFS(1)
print(len(path)-1)