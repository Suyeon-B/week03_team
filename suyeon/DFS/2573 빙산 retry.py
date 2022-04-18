import sys
from collections import deque
sys.stdin = open("DFS/input.txt",'r')
input = sys.stdin.readline

# 이차원 배열의 크기 m, n
n, m = map(int, input().strip().split())

# 좌표
dx = [-1, 1, 0, 0] # 서동북남 순서
dy = [0, 0, -1, 1]

# 빙산 정보 table
iceberg_and_sea = [list(map(int, input().strip().split())) for _ in range(n)]
icebergs = deque()
devided = False
year = 0

# (a, b) 좌표부터 시작해서 bfs
# 덩어리 갯수를 세어준다.
def bfs(a, b):
    icebergs.append((a, b))
    while icebergs:
        x, y = icebergs.popleft() # 빙산의 좌표 꺼내기
        visited[x][y] = True
        for i in range(4): # 동서남북 돌면서 바다와 만나면 빙산 녹이기
            new_x, new_y = x+dx[i], y+dy[i]
            # 새로운 좌표가 table 안에 포함되고,
            if 0<=new_x<n and 0<=new_y<m:
                # 아직 방문 전인 빙산(숫자)이면
                if iceberg_and_sea[new_x][new_y] != 0 and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    icebergs.append((new_x, new_y))
                # 바다이면 
                elif iceberg_and_sea[new_x][new_y] == 0:
                    melting_count[x][y] += 1 # melting_count에 빙산 녹일만큼 count
            
    return 1

# 빙산이 분리될 때 까지 bfs 반복
while True:
    result = []
    visited = [[False]*m for _ in range(n)]
    melting_count = [[0]*m for _ in range(n)]
    
    # 빙산 개수 count
    for i in range(n):
         for j in range(m):
            if not visited[i][j] and iceberg_and_sea[i][j] != 0: # 방문한 적 없고, 바다가 아니면 bfs 돌면서 깎을 빙산 체크
                result.append(bfs(i, j))
                
    # 빙산 깎기
    for i in range(1, n):
        for j in range(1, m):
            iceberg_and_sea[i][j] -= melting_count[i][j]
            if iceberg_and_sea[i][j] < 0:
                iceberg_and_sea[i][j] = 0

    if len(result) == 0:
        break

    if len(result) >= 2:
        devided = True
        break
    year += 1

if devided:
    print(year)
else:
    print(0)
