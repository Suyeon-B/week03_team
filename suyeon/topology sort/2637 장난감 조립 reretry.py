import sys
from collections import deque, defaultdict
sys.stdin = open("topology sort/input.txt",'r')
input = sys.stdin.readline

# 정점의 개수 v, 간선의 개수 e
v = int(input().strip())
e = int(input().strip())

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
outdegree = [0] * (v+1)

graph = [[] for i in range(v+1)]
elements = [0] * (v+1)
# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    indegree[b] += 1
    outdegree[a] += 1

# 위상 정렬 함수
def topology_sort():
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용
    basic = defaultdict(int)
    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
        if outdegree[i] == 0:
            basic[i] = i

    elements[v] = 1 
    # 큐가 빌 때 까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입 차수에서 1 빼기
        for next, cnt in graph[now]:
            elements[next] += elements[now] * cnt
            indegree[next] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[next] == 0:
                q.append(next)
    # 위상 정렬을 수행한 결과 출력
    for bc in basic:
        print(bc, elements[bc])

topology_sort()