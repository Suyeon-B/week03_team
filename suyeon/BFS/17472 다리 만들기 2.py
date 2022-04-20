# 실패
"""
모든 섬을 연결하는 다리 길이의 최솟값 구하기

조건
1. 모든 섬을 연결하는 것이 불가능하면 -1 출력
2. 다리 길이는 2 이상
3. 다리는 중간에 방향 전환 불가

IDEA
1. 우선 땅이 먼저 나오는 곳에서 bfs 탐색 시작
    dictionary[땅의 번호] = 좌표들 로 저장함
2. 섬 번호대로 bfs 탐색 중에 다른 땅의 x, y좌표가 같으면 한 칸씩 이동하며 다리 길이 +1
    연결된 애는 다음 번에 bfs 탐색하지 않음
3. 만약 다 돌았는데 다리의 개수 < (섬의개수 - 1) 이면 -1 출력
4. 아니라면 다리길이 출력
"""

import sys, collections
from collections import deque
input = sys.stdin.readline

# 세로 크기 N과 가로 크기 M
n, m = map(int, input().strip().split())

# 섬 dictionary
island_id = [6, 5, 4, 3, 2, 1] # 섬의 개수 stack - dictionary key 용 / 2 ≤ 섬의 개수 ≤ 6
island = collections.defaultdict(list)

# 지도
MAP = [list(map(int, input().strip().split())) for _ in range(n)]
bridge = [[0]*(m+1) for _ in range(n+1)]

# 좌표 이동용
dx = [1, -1, 0, 0] # 동서남북 순
dy = [0, 0, 1, -1]

# (a, b)에서부터 bfs로 땅 찾기
def bfs_find_island(a, b):
    # 방문 처리
    visited[a][b] = True
    # 큐 생성
    q = deque((a, b)) # 시작 값 큐에 append
    # 딕셔너리 update
    ID = island_id.pop()
    island[ID] += (a, b)
    # bfs 시작
    while q:
        x, y = q.popleft() # 다음 좌표 꺼내기
        for i in range(4): # 동서남북 돌면서 땅 찾기
            nx, ny = x+dx[i], y+dy[i]
            # 새로운 좌표가 MAP 안에 들어가고, 바다가 아니라면
            if 0<=nx<n and 0<=ny<m and MAP[nx][ny] == 1:
                visited[nx][ny] = True
                island[ID] += (nx, ny)

def bfs_build_bridge(id):
    # 탐색 시작할 맨 앞 좌표 꺼내기
    x, y = island[id][0][0], island[id][0][1]
    # visited[x][y] = True
    q = deque((x, y)) # 시작 값 큐에 append
    # bfs 시작
    while q:
        # 다른 땅의 x, y좌표가 같아지는 지점인지 확인
        for i in range(len(island[id])): # 섬의 크기만큼 돌며 찾는다.
            x, y = q.popleft() # 다음 좌표 꺼내기
            for another_land_id in range(1, len(island)+1):
                if another_land_id != id: # 다른 땅
                    for j in range(len(island[another_land_id])):
                        length = 0
                        an_x, an_y = island[another_land_id][j][0], island[another_land_id][j][1]
                        if x == an_x: # 가로로 길을 놓을 수 있을 때
                            pass
                            # 가로 길을 놓고.. 각 가로 길들의 max를 구하고.. 백퍼 시간초과이기 때문에 여기서 멈춥니다 ^^ㅎ





# 1. 우선 땅이 어딨나 체크해서 dictionary[땅의 번호] = 좌표들 로 저장함
visited = [[False]*m for _ in range(n)]
for x in range(n):
    for y in range(m):
        if MAP[x][y] != 0 and not visited[x][y]:
            bfs_find_island(x, y)

# 2. 섬 dictionary 번호대로 bfs 탐색 시작 
# 돌면서 다른 땅의 x, y좌표가 같아지는 지점에서 한 칸씩 이동하며 다리 길이 +1
# 연결된 애는 다음 번에 bfs 탐색하지 않음
# visited = [[False]*m for _ in range(n)] 
IDs = island.keys()
for id in IDs:
    bfs_build_bridge(id)
