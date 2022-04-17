import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

iceberg = []
for i in range(N):
    iceberg.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    Q = deque([[x, y]])
    visited[x][y] = True
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[nx][ny]: continue
            if iceberg[nx][ny] <= 0:
                iceberg[x][y] -= 1
            else:
                visited[nx][ny] = True
                Q.append([nx, ny])


T = 0

while True:
    cnt = 0
    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if iceberg[i][j] > 0 and not visited[i][j]:
                bfs(i,j)
                cnt += 1

    if cnt == 0:
        T =0
        break
    if cnt > 1:
        break
    T+=1


print(T)