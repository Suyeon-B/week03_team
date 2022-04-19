import sys
from collections import deque

sys.stdin = open('input.txt')
R, C = map(int, sys.stdin.readline().split())
board = []
visited = [[-1] * C for _ in range(R)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = 1e6


def spread_water():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if board[nx][ny] == '.' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1;
                queue.append((nx, ny))


def move():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue
            if board[nx][ny] == 'D':
                print(visited[x][y] + 1)
                exit(0)
            if board[nx][ny] == '.' and (visited[nx][ny] == -1 or visited[x][y] + 1 < visited[nx][ny]):
                visited[nx][ny] = visited[x][y] + 1;
                queue.append((nx, ny))


def print_result():
    for i in range(R):
        for j in range(C):
            print(visited[i][j], end=' ')
        print()


for _ in range(R):
    s = sys.stdin.readline()
    board.append(s)

queue = deque()
flag = False
for i in range(R):
    for j in range(C):
        if board[i][j] == '*':
            queue.append((i, j))
            visited[i][j] = 0
            flag = True
            break
    if flag == True:
        break

spread_water()

flag = False
for i in range(R):
    for j in range(C):
        if board[i][j] == 'S':
            queue.append((i, j))
            visited[i][j] = 0
            flag = True
            break
    if flag == True:
        break

move()

print("KAKTUS")
