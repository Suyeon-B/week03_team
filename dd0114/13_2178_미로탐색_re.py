# 왜왜왜왜 방문검색과 미로 검색 둘다 하는게 더 빠른지
import sys
import copy
from collections import deque
sys.setrecursionlimit(10**6)

n, m = map(int,sys.stdin.readline().split())
maze = []

for i in range(n):
    maze.append(list(map(int,sys.stdin.readline().strip())))

visited = [[0]* m for _ in range(n)]
qlist = [[0,0]]

dy = (1,0,-1,0)
dx = (0,1,0,-1)
visited[0][0] = 1 

while qlist :
    y, x =qlist.pop(0)
    for i in range(4):
        ny,nx = y+dy[i],x+dx[i]
        
        if   m-1 >= nx>=0 and n-1 >= ny>=0 :
            if maze[ny][nx]==1 and visited[ny][nx] == 0:
                qlist.append([ny,nx])
                visited[ny][nx] = visited[y][x] +1

print(visited[n-1][m-1])