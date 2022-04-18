from pydoc import doc
import sys
import copy
from collections import deque
sys.setrecursionlimit(10**6)

n, m = map(int,input().split())
maze = []

for i in range(n):
    a = list(map(int,sys.stdin.readline().strip()))
    maze.append(a)

visited = copy.deepcopy(maze)
qlist = deque([])
qlist.append([0,0])

dy = (1,0,-1,0)
dx = (0,1,0,-1)
length = [[0]*m for _ in range(n)]
length[0][0] = 1

while qlist :
    y, x =qlist.popleft()
    visited [y][x] = 0

    for i in range(4):
        ny,nx = y+dy[i],x+dx[i]
        
        if   m-1 >= nx>=0 and n-1 >= ny>=0 and visited[ny][nx] :
            qlist.append([ny,nx])
            length[ny][nx] = length[y][x] +1

print(length[n-1][m-1])