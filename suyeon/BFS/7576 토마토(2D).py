import sys
from collections import deque
sys.stdin = open("BFS/input.txt",'r')
input = sys.stdin.readline

# 상자의 크기 m, n
m, n = map(int, input().strip().split())

# 좌표
dx = [1, -1, 0, 0] # 동서남북 순
dy = [0, 0, 1, -1]


# 토마토 정보 table
# 익은 토마토 : 1 / 안 익은 토마토 : 0 / 없음 : -1
tomatoes = [list(map(int, input().strip().split())) for _ in range(n)]

# 큐에 익은 토마토 넣기 (bfs 시작용)
ripe_tomatoes = deque([])
for x in range(n):
    for y in range(m):
        if tomatoes[x][y] == 1: # 익은 토마토이면
            ripe_tomatoes.append([x, y]) # 큐에 토마토의 좌표를 넣는다.

# BFS
def make_ripe():
    while ripe_tomatoes:
        x, y = ripe_tomatoes.popleft() # 익은 토마토의 좌표 꺼내기
        for i in range(4): # 동서남북 돌면서 토마토 익히기
            new_x, new_y = x+dx[i], y+dy[i]
            # 새로운 좌표가 토마토 상자 안에 포함되면 & 토마토가 안 익은 토마토이면
            if 0<=new_x<n and 0<=new_y<m and tomatoes[new_x][new_y] == 0:
                tomatoes[new_x][new_y] = tomatoes[x][y] + 1 # 토마토 익히고 익은 토마토에 +1해서 넣기 (year 기록용)
                ripe_tomatoes.append([new_x, new_y])

def check():
    result = 0
    # tomatoes 판 돌면서 안 익은 애 남아있나 확인
    for line in tomatoes:
        for tomato in line:
            if tomato == 0: # 익은 토마토이면
                print(-1)
                exit(0)
        result = max(result, max(line))
    print(result-1)
make_ripe()
check()