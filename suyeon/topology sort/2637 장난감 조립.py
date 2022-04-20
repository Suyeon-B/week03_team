# 수정 중인 코드입니다.
import sys
from collections import deque, defaultdict
sys.stdin = open("topology sort/input.txt",'r')
input = sys.stdin.readline

# 정점(부품)의 개수 n, 간선(부품들 간의 관계)의 개수 m
n, m = int(input().strip()), int(input().strip())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (n+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(n+1)]
# 연결 정보
connect = [[] for _ in range(n+1)]


# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(m):
    a, b, c = map(int, input().strip().split())
    graph[b].append((a, c))
    # indegree[a] += c
    indegree[a] += 1

# 위상 정렬 함수
def topology_sort():
    q = deque()
    # 처음 시작 시, 진입차수가 0인 것들을 큐에 담는다.
    for i in range(1, n+1):
        if indegree[i] == 0: # 이 때 진입차수가 0인 것들이 기본 부품이다.
            q.append(i)
            basic[i] = 1

    # total = collections.defaultdict(int)
    # 큐가 빌 때 까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
        # for neighbor, cost in graph[now]: # now -> neighbor는 cost만큼의 부품이 필요하다
        #     # 기본 부품이 아니라면
        #     # 이전 단계 cost와 곱한 값이 cost이다.
        #     last = graph[now]
        #     if not basic[now]:
        #         last = graph[last]
        #         cost *= total*last[1]
        #         del basic[now]
        #     indegree[neighbor] -= cost
        #     if indegree[neighbor] == 0:
        #             q.append(neighbor)
        # 같은 단계 cost끼리는 더한다.
        # total[last] = cost
    
    keys = cnt.keys()
    # 위상 정렬을 수행한 결과
    for i in keys:
        print(f'{i} {cnt[i]}')

result = [0]*len(basic)


topology_sort()
