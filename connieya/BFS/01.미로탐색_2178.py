import sys
N,M = map(int,sys.stdin.readline().split())
maze = [[0]*M for i in range(N)]
visited = [ [-1]*M for i in range(N)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]
for i in range(N):
   str = sys.stdin.readline()
   for j in range(M):
       maze[i][j] = int(str[j])


queue = []
queue.append((0,0))
visited[0][0] = 1
while queue:
    x,y = queue.pop(0)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >=N or ny < 0 or ny >=M: continue
        if maze[nx][ny] == 1 and visited[nx][ny] == -1:
            visited[nx][ny] = visited[x][y]+1
            queue.append((nx,ny))


print(visited[N-1][M-1])