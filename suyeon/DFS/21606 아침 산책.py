# 부분 성공
# 조합론 적용 필요
import sys
sys.stdin = open("DFS/input.txt",'r')
input = sys.stdin.readline
path = 0

def dfs(start_node, visited, graph, is_indoor):
    global path
    visited[start_node] = True
    for v in graph[start_node]:
        if not visited[v]:
            if is_indoor[0][v-1] == '1': # 실내를 만나면 경로 개수 추가
                path+=2
                visited[start_node] = visited[v] = False
                return
            # 실외를 만나면 더 깊이 탐색
            else:
                dfs(v, visited, graph, is_indoor)

def main():
    global path
    n = int(input().strip()) # 정점의 개수 n
    is_indoor = list(map(str, input().split())) # 실내: 1, 실외: 0

    # graph & visited 정보 저장
    graph = [[] for _ in range(n+1)]
    for i in range(n-1):
        vertex1, vertex2 = map(int, input().strip().split())
        graph[vertex1] += [vertex2]
        graph[vertex2] += [vertex1]
    visited = [False] * (n+1)

    # 실내 중에 시작점 정해서 또 다른 실내를 만날 때 까지 dfs
    for v in range(1, n+1): # 모든 노드를 시작점의 후보로
        if not visited[v]:
            if is_indoor[0][v-1] == '1': # 실내이면 dfs 시작
                dfs(v, visited, graph, is_indoor)
    print(path)

main()

