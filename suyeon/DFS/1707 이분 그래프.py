# 시간초과 해결 필요
import sys, collections
sys.setrecursionlimit(10**6) # python RecursionError 방지
input = sys.stdin.readline
check_bipartite = True
# 색깔 체크용 변수 설정
RED = 1
BLUE = -1
        
def DFS(start_node, color, graph, colors, visited):
    colors[start_node] = color
    visited[start_node] = True

    for v in graph[start_node]:
        if not visited[v]: # 방문하지 않았으면
            next = DFS(v, -color, graph, colors, visited)
            if not next:
                return False
        elif colors[v] == colors[start_node]:
            return False
    return True

# 테스트 케이스의 개수
k = int(input().strip())

for i in range(k):
    # 정점의 개수 V / 간선의 개수 E
    V, E = map(int, input().strip().split())
    colors = [0] * (V+1)
    visited = [False] * (V+1)

    # k번째 테스트케이스 그래프
    graph = [[] for i in range(V+1)]
    for _ in range(1, E+1):
        vertex1, vertex2 = map(int, input().split())
        graph[vertex1] += [vertex2]
        graph[vertex2] += [vertex1] # 무방향 그래프이므로
        
    # 연결그래프와 비연결그래프 모두를 고려하기 위해
    # 모든 정점을 돈다.
    for v in range(1, V+1):
        if not visited[v]:
            result = DFS(v, RED, graph, colors, visited)
            if not result:
                break
    
    # 결과 출력
    print('YES' if result else 'NO')