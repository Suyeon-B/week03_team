# 인접행렬 ver
import sys
sys.stdin = open("DFS/input.txt",'r')
sys.setrecursionlimit(10**6) # python RecursionError 방지
input = sys.stdin.readline
# 색깔 체크용 변수 설정
RED = 1
BLUE = -1
        
def DFS(start_node, color, colors):
    visited[start_node] = True
    colors[start_node] = color
    for v in graph[start_node]:
        if not visited[v]: # 방문 전이라면
            DFS(v, -color, colors) # 인접노드와 다른 색을 칠해준다.

    return colors

# test case 개수
k = int(input().strip())

# test case 개수 만큼 이분 그래프 여부 따짐
for i in range(k):
    # 정점의 개수 V / 간선의 개수 E
    V, E = map(int, input().strip().split())

    # visited[v] = False -> v 정점은 방문 전이라는 의미
    visited = [False] * (V+1)

    # 정점의 색깔
    colors = [0] * (V+1)

    # 간선의 개수만큼 그래프에 반영
    graph = [[] for i in range(V+1)]
    for v in range(1, E+1):
        vertex1, vertex2 = map(int, input().strip().split())
        graph[vertex1].append(vertex2)
        graph[vertex2].append(vertex1)
    
    # DFS로 color 칠해줌
    color = RED # 초기 색깔은 빨간색
    for v in range(1, V+1):
        if not visited[v]:
            colors = DFS(v, color, colors)
    
    breaker = False
    for v in range(1, V):
        for node in graph[v]:
            if colors[node] == colors[v]: # 인접노드와 색깔이 같으면
                result = "NO"
                breaker = True
                break
            else:
                result = "YES"
        if breaker:
            break
    
    print(result)