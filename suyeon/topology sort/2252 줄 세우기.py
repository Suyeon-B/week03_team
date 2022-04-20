import sys
from collections import deque

sys.stdin = open("topology sort/input.txt",'r')
input = sys.stdin.readline

# 정점(학생)의 개수 n, 간선(학생의 키 비교)의 개수 m
n, m = map(int, input().strip().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(n+1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(m):
    a, b = map(int, input().strip().split())
    graph[a].append(b)
    indegree[b] += 1

# 위상 정렬 함수
def topology_sort():
    q = deque()
    result = []
    # 처음 시작 시, 진입차수가 0인 것들을 큐에 담는다.
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
    # 큐가 빌 때 까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 건 큐에 넣어줌
            if indegree[i] == 0:
                q.append(i)
    
    # 위상 정렬을 수행한 결과
    for i in result:
        print(i, end=" ")

topology_sort()
