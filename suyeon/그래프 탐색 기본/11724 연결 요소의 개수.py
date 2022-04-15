# visited를 미리 배열로 지정해주어 시간 복잡도 개선
import sys, collections
sys.setrecursionlimit(10**6) # python RecursionError 방지
input = sys.stdin.readline

n, m = map(int, input().split())

graph = collections.defaultdict(list) # 빈 그래프 생성, default는 list
for i in range(1, m+1):
    vertex1, vertex2 = map(int, input().split())
    graph[vertex1] = graph[vertex1]+[vertex2]
    graph[vertex2] = graph[vertex2]+[vertex1] # 무방향 그래프이므로

# recursive DFS
visited = [False] * (n+1)
def DFS(start_v):
    visited[start_v] = True
    for v in graph[start_v]:
        if not visited[v]:
            DFS(v)

DFS(1) # 시작 노드는 항상 1이다.

# Connected component 개수 구하기
cnt = 1
for i in range(1, n+1):
    if not visited[i]:
        DFS(i) # 아직 탐색하지 않은 노드를 시작노드로 다시 Connected component 찾기
        cnt+=1

print(cnt)