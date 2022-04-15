# 프림의 알고리즘 사용
# heap 자료구조와 함께 사용해 시간 복잡도 N(ElogE)
# 1 ≤ E ≤ 100,000 이므로 제한 시간 내에 가능

# defaultdict 추가 공부 필요
# 크루스칼 알고리즘 복기 필요

import heapq, sys, collections
input = sys.stdin.readline

n, m = map(int, input().strip().split()) # 노드 수, 간선 수
graph = collections.defaultdict(list) # 빈 그래프 생성, default는 list
visited = [0]*(n+1) # 노드 방문 정보 초기화

# 무방향 그래프 생성
for i in range(m):
    u, v, weight = map(int, input().strip().split())
    # 궁금한 부분
    graph[u].append([weight, u, v])
    graph[v].append([weight, v, u])

# 프림 알고리즘
def prim(graph, start_node):
    visited[start_node] = 1
    # 인접 간선 추출
    candidate = graph[start_node]
    # 우선순위 큐 생성
    heapq.heapify(candidate)
    # mst 저장할 배열
    mst = []
    # 전체 가중치
    total_weight = 0

    # while 인접 간선이 있을 때
    while candidate:
        # 가중치가 가장 적은 간선 추출
        weight, u, v = heapq.heappop(candidate)
        # 방문하지 않았다면
        if visited[v] == 0:
            # 방문 갱신
            visited[v] = 1
            # mst 삽입
            mst.append((u, v))
            # 전체 가중치 갱신
            total_weight += weight

            # 다음 인접간선 탐색
            for edge in graph[v]:
            # 방문한 노드가 아니라면, (cycle 방지)
                if visited[edge[2]] == 0:
                    # 우선순위 큐에 edge 삽입
                    heapq.heappush(candidate, edge)

    # total weight return
    return total_weight

# 결과 출력
print(prim(graph, 1))