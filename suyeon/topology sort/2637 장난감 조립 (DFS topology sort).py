from collections import defaultdict
import sys

sys.stdin = open("topology sort/input.txt",'r')
input = sys.stdin.readline

# 정점(부품)의 개수 n, 간선(부품들 간의 관계)의 개수 m
n = int(input().strip())
m = int(input().strip())
# 방문 정보
visited = [False] * (n+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = defaultdict(int)
for i in range(1, n+1):
    vertex2, vertex1, cost = map(int, input().strip().split())
    graph[vertex1] = [vertex2, cost] # vertex1 -> vertex2 가는데 비용이 cost

total = 0
def topology_sort(start_v, last):
    global total
    if not visited[start_v]:
        visited[start_v] = True
        for neighbor, cost in graph[start_v]:
            cost *= last
            last = cost
            topology_sort(neighbor, last)
    
