import sys

n = int(sys.stdin.readline())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
INF = 1e7
board = [[0] * n for i in range(n)]
visited = [[INF] * n for i in range(n)]
for i in range(n):
    str = sys.stdin.readline()
    for j in range(n):
        board[i][j] = int(str[j])

q = []
q.append((0, 0))
visited[0][0] = 0

while q:
    x, y = q.pop(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n: continue
        if board[nx][ny] == 1:
            if visited[nx][ny] > visited[x][y]:
                visited[nx][ny] = visited[x][y]
                q.append((nx, ny))
        else:
            if visited[nx][ny] > visited[x][y] + 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

print(visited[n - 1][n - 1])
