import heapq
import sys, collections
sys.stdin = open("BFS/input.txt",'r')
input = sys.stdin.readline

# 도시의 개수 N(1 ≤ N ≤ 1,000), 버스의 개수 M(1 ≤ M ≤ 100,000)
n, m = int(input().strip()), int(input().strip())


# weights = [출발, 끝, 가중치]
def min_cost(weights, start, end):
    graph = collections.defaultdict(list)
    # 그래프 인접리스트 구성
    for u, v, w in weights:
        graph[u].append((v, w))

    # 큐 변수 : [(소요 시간, 정점)]
    q = [(0, start)]
    dist = collections.defaultdict(int)

    # 우선순위 큐 최솟값 기준으로 정점까지 최단 경로 삽입
    while q:
        weight, node = heapq.heappop(q)
        if node not in dist:
            dist[node] = weight
            for v, w in graph[node]:
                alt = weight + w
                heapq.heappush(q, (alt, v))
        if node == end:
            return max(dist.values())

weights = [list(map(int, input().strip().split())) for _ in range(m)]
start, end = map(int, input().strip().split())

print(min_cost(weights, start, end))