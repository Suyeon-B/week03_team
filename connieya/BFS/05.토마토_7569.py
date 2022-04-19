import sys
from collections import deque

column, row, height = map(int, sys.stdin.readline().split())
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]
tomato = []
for i in range(height):
    layer = []
    for j in range(row):
        layer.append(list(map(int,sys.stdin.readline().split())))
    tomato.append(layer)

queue = deque()
total = 0
for k in range(height):
    for i in range(row):
        for j in range(column):
            if tomato[k][i][j] == 1:
                queue.append((k, i, j, 0))
            elif tomato[k][i][j] == -1:
                total += 1

day = 0
while queue:
    h, r, c, cnt = queue.popleft()
    total += 1
    day = cnt
    for i in range(6):
        nx = r + dx[i]
        ny = c + dy[i]
        nh = h + dh[i]
        if nx < 0 or nx >= row or ny < 0 or ny >= column or nh < 0 or nh >=height:
            continue
        if tomato[nh][nx][ny] == 0:
            tomato[nh][nx][ny] =1
            queue.append((nh,nx,ny,cnt+1))

if total == row*height*column:
    print(day)
else:
    print(-1)