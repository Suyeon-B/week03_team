# 이 파일 말고 retry 파일만 보면 됩니당~ 
# 빙산 count하려면
# 빙산이 남아 있는 부분에서 다시 BFS를 해야하므로,
# BFS 코드에서는 주변에 바다가 몇 개 있는지만 세며 방문한 노드 처리를 해주고,
# BFS 탐색한 덩어리 갯수를 따져주며 반복해야 함.


import sys
from collections import deque
sys.stdin = open("DFS/input.txt",'r')
input = sys.stdin.readline

# 이차원 배열의 크기 m, n
m, n = map(int, input().strip().split())

# 좌표
dy = [1, -1, 0, 0] # 동서남북 순
dx = [0, 0, 1, -1]

# 빙산 정보 table / temp는 BFS에서 바로 반영하지 않기 위함
iceberg_and_sea = [list(map(int, input().strip().split())) for _ in range(m)]
temp = iceberg_and_sea
visited = [[False]*n for _ in range(m)]

# 큐에 빙산 정보 넣기 (bfs 시작용)
icebergs = deque([])
for x in range(1, m):
    for y in range(1, n):
        if iceberg_and_sea[x][y] != 0: # 빙산이면
            icebergs.append([x, y]) # 큐에 빙산의 좌표를 넣는다.

# BFS
def melt():
    global iceberg_and_sea
    year = 0
    while icebergs:
        x, y = icebergs.popleft() # 빙산의 좌표 꺼내기
        visited[x][y] = True
        year += 1
        for i in range(4): # 동서남북 돌면서 바다와 만나면 빙산 녹이기
            new_x, new_y = x+dx[i], y+dy[i]
            # 새로운 좌표가 table 안에 포함되고, 빙산(숫자)이 아닌 바다(0)이면
            if 0<=new_x<=n and 0<=new_y<=m and iceberg_and_sea[new_x][new_y] == 0:
                temp[x][y] -= 1 # temp table의 빙산 1만큼 녹이기
                visited[x][y] = True
                # 녹였더니 바다가 됐으면
                if temp[x][y] == 0:
                    # 남은 빙산 좌표들이 몇 덩어리인지 센다.
                    cnt = count()
                    if cnt >= 2: # 2개 이상으로 나뉘면 year return
                        return year
        iceberg_and_sea = temp # 바뀐 빙산 정보 반영
    # return 0 # 끝까지 분리되지 않으면 0 return


# 빙산이 count
# def count():
#     for i in range(m):
#         for j in range(n):
#             if temp[i][j]


print(melt())