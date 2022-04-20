import sys
from collections import deque
sys.stdin = open("BFS/input.txt",'r')
input = sys.stdin.readline

# R행 C열
r, c = map(int, input().strip().split())
MAP = []
visited = [[-1]*c for _ in range(r)] # 물 0, 고슴 1 / 미방문 -1

# 좌표이동용
move = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 고슴도치와 물 시작지점
sündisznó = deque()
víz = deque()
time = 0
end = False

# MAP 세팅 & 좌표 탐색
for row in range(r):
    temp = str(input().strip())
    MAP.append(temp)
    for col in range(c):
        # 고슴이 위치 sündisznó
        if temp[col] == 'S':
            sündisznó.append((row, col))
        # 물 시작지점
        elif temp[col] == '*':
            víz.append((row, col)) 

def bfs_sündisznó():
    global end, time
    size = len(sündisznó)
    while size>0:
        try:
            size-=1
            x, y = sündisznó.popleft()
            visited[x][y] = 1
            for a, b in move:
                nx, ny = x+a, y+b
                # 물이 없고 돌이 없는 곳이면
                if 0<=nx<r and 0<=ny<c:
                    if MAP[nx][ny] == "D":
                        end = True
                        return
                    elif visited[nx][ny] != 0 and visited[nx][ny] != 1 and MAP[nx][ny] != "X":
                        visited[nx][ny] = 1 # 고슴이 이동하고
                        sündisznó.append((nx, ny)) # 큐에 넣는다
        except:
            print("KAKTUS")
            exit(0)

def bfs_víz():
    size = len(víz)
    while size>0:
        x, y = víz.popleft()
        visited[x][y] = 0
        size-=1
        for a, b in move:
            nx, ny = x+a, y+b
            # 돌이나 비버 집이 없는 빈 곳이면
            if 0<=nx<r and 0<=ny<c and visited[nx][ny] != 0 and MAP[nx][ny] != "X" and MAP[nx][ny] != "D":
                visited[nx][ny] = 0 # 물 채우고
                víz.append((nx, ny)) # 큐에 넣는다
                # 시작하자마자 물로 고슴이 채워버리면 안됨
                if time == 0:
                    if MAP[nx][ny] == "S":
                        visited[nx][ny] = -1 # 다시 물 뺌

def main():
    while True:
        bfs_víz()
        bfs_sündisznó()
        global time
        time += 1
        if end:
            print(time)
            exit(0)
        if not sündisznó:
            print("KAKTUS")
            exit(0)

main()