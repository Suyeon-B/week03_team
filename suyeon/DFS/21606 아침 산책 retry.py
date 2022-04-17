# 73점
# 시간 복잡도 개선 필요
import sys
sys.stdin = open("DFS/input.txt",'r')
input = sys.stdin.readline
path = 0

def dfs(start_node, visited, graph, is_indoor):
    visited[start_node] = True
    result = 0
    for v in graph[start_node]:
        if not visited[v]:
            # start_node가 실외일 때, 주변에 있는 실내 노드 v들을 count한다.
            if is_indoor[0][v-1] == '0':
                result += dfs(v, visited, graph, is_indoor)
            else: # start_node가 실내일 때, 주변에 있는 실내 노드 v들을 count한다.
                result += 1
    return result

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
        if is_indoor[0][v-1] == '1': # 실내일 때
            for j in graph[v]:
                if is_indoor[0][j-1] == '1':
                    path += 1
        else:
            if visited[v]:
                continue
            temp = dfs(v, visited, graph, is_indoor)
            path += temp * (temp-1)
        
    print(path)

main()

